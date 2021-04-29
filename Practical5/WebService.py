from flask import Flask, render_template

import smtplib
import json

from email.message import EmailMessage

from flask.globals import request


from Cmd_implementation import generate_matrix, apply_TOPSIS, write_result_in_output_file

##########################################################################

def get_email_and_password(config_file_path):

    config_file = open(config_file_path)
    
    config_file_content = config_file.read()

    credentials = json.loads(config_file_content)

    MY_EMAIL = credentials['email']
    
    MY_PASSWORD = credentials['password']

    return MY_EMAIL, MY_PASSWORD


########################################################################

def construct_email_message(from_ ,to_, attachments) -> EmailMessage:

    msg = EmailMessage()

    msg['Subject'] = "TOPSIS algorithm implementation in PYTHON"

    msg['From'] = from_

    msg['To'] = to_

    for attachment in attachments:

        with open(attachment, 'rb') as new_attachment:

            content = new_attachment.read()

            msg.add_attachment(content, maintype='application', subtype='octet-stream', filename = attachment)


    return msg


############# Only problem left is that the files are getting deleted and do not hold any content ############## 
############ Why is it happeing ###############################################################################


def send_email(recipient_email, result_filename):

    # Read email and password from config
    MY_EMAIL, MY_PASSWORD = get_email_and_password('config.json')

    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        # Have an smtp connection
        code, status = smtp.login(MY_EMAIL, MY_PASSWORD)

        if code == 235:
            print('Successfully logged in to google')
        
            msg = construct_email_message(MY_EMAIL, recipient_email, [result_filename])

            smtp.send_message(msg)

        smtp.close()

    #1 -> Login using your email and password


def run_service(input_data, weights, impacts, user_email):
    # input_data, weights, impacts, user_email = get_user_input()
    weights = [float(val) for val in weights.split(',')]

    impacts = impacts.split(',')
    
    input_data_copy = input_data.copy()
    
    input_matrix = generate_matrix(input_data)
    
    output_filename = 'output.csv'
    
    performance_score, ranks = apply_TOPSIS(input_matrix, weights, impacts)
    
    write_result_in_output_file(input_data_copy, performance_score, ranks, output_filename)
    # use input_matrix to generate  output_filesend_email(user_email, output_filename)
    send_email(user_email, output_filename)




################# ADD VALIDATION TO THE FLASK REQUEST OBJET #####################

##################### MAKE IT A FLASK APP ################

##### Lets create an app here
app = Flask(__name__)

def is_file_valid(filename):
    allowed_extensions = ['txt', 'csv']

    if not filename:
        return False

    file_extension = filename[-3:]
    return file_extension in allowed_extensions


############### Configure an upload path for files
UPLOAD_FOLDER = "/home/rishabh/Documents/course_work/8th_sem/lab_practical/data_mining_lab/Practical5/Lab Assignment 05/Input files for Assignment05/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import os
# from werkzeug.utils import secure_filename
######## make a default rou
def validate(input_data, weights, impacts, user_email):
    errors = []

    ##################### check if weights are valid #######
    ## find non negative value in weights
    weights_copy = weights.split(',')
    # def is_valid_weight(w):
    #     return isinstance(w, int) or isinstance(w, float)

    # non_numerical_weights = [val for val in weights_copy if not is_valid_weight(val)] ## type(va)
    # if non_numerical_weights:
    #     errors.append("Weights can be numerical values only")
    try:
        [float(val) for val in weights_copy]
    except ValueError:
        errors.append("Weights can be numerical values only")
    
    ########### validity of impacts ###########
    impacts_copy = impacts.split(',')
    def is_valid_impact(i):
            return i in ['+', '-']

    invalid_impacts = [val for val in impacts_copy if (not is_valid_impact(val))]

    if invalid_impacts:
        errors.append(f"Invalid value for an impact : {invalid_impacts[0]}")

    ################### number of columns in input_file ########
    input_data_copy = input_data.copy()

    input_matrix = generate_matrix(input_data_copy)

    if len(input_matrix[0]) < 3:
        errors.append(f'Input file should have atleast 3 columns, your file only had {len(input_matrix[0])}')


    ################# check for dimensionality of the data, weights, and impacts
    if (len(weights_copy) != len(impacts_copy)) or (len(weights_copy) != len(input_matrix[0])):
        errors.append(f'Weights, Impacts and Input Data should have same number of columns')


    ####### check if user email looks nice
    ######### can use regex match
    print(errors)
    
    return errors




@app.route('/', methods = ['POST', 'GET'])
def default_page():
    if request.method == 'POST':
        data_file = request.files['file-content']
        
        if is_file_valid(data_file.filename):
            
            res_path = os.path.join(app.config['UPLOAD_FOLDER'], data_file.filename)

            data_file.save(res_path)

            ########## get input_data, weights, impacts, user_email
            input_data = open(res_path).read().strip('\n').split('\n')

            weights = request.form['weights']

            impacts = request.form['impacts']

            user_email = request.form['email']

            ########### validate these ################
            ##########3 if errors, return errors
            ############# else run service
            errors = validate(input_data, weights, impacts, user_email)
            print("--------------------------------------------------------")
            print("--------------------------------------------------------")
            print(errors)
            print("--------------------------------------------------------")
            print("--------------------------------------------------------")


            if errors:
                return render_template('data_form.html', my_errors = errors)

            run_service(input_data, weights, impacts, user_email)

            return render_template('success_message.html')


        else:
            return render_template('data_form.html')

        

    else:
        return render_template('data_form.html')




def main():

    # Take a file and an email from the command line
    # run_service()
    app.run(debug=True)



if __name__ == "__main__":
    main()


####### JUST ADD FLASK UI TO IT AND ITS GOOD TO GO #########