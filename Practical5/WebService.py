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
    
    input_data_copy = input_data.copy()
    
    input_matrix = generate_matrix(input_data)
    
    output_filename = 'output.csv'
    
    performance_score, ranks = apply_TOPSIS(input_matrix, weights, impacts)
    
    write_result_in_output_file(input_data_copy, performance_score, ranks, output_filename)
    # use input_matrix to generate  output_filesend_email(user_email, output_filename)
    send_email(user_email, output_filename)





##################### MAKE IT A FLASK APP ################

##### Lets create an app here
app = Flask(__name__)

def is_file_valid(filename):
    allowed_extensions = ['txt', 'csv']

    if len(filename) == 0:
        return False

    file_extension = filename[-3:]
    return file_extension in allowed_extensions


############### Configure an upload path for files
UPLOAD_FOLDER = "/home/rishabh/Documents/course_work/8th_sem/lab_practical/data_mining_lab/Practical5/Lab Assignment 05/Input files for Assignment05/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import os
# from werkzeug.utils import secure_filename
######## make a default route
@app.route('/', methods = ['POST', 'GET'])
def default_page():
    if request.method == 'POST':
        data_file = request.files['file-content']
        
        if is_file_valid(data_file.filename):
            res_path = os.path.join(app.config['UPLOAD_FOLDER'], data_file.filename)

            data_file.save(res_path)

            ########## get input_data, weights, impacts, user_email
            input_data = open(res_path).read().strip('\n').split('\n')

            weights = [float(val) for val in request.form['weights'].split(',')]

            impacts = request.form['impacts'].split(',')

            user_email = request.form['email']

            run_service(input_data, weights, impacts, user_email)

            return "Congratulations... Output has been sent to your email"


        else:
            return "ERROR OCCURED.. You can upload only csv or txt files"

        

    else:
        return render_template('data_form.html')




def main():

    # Take a file and an email from the command line
    # run_service()
    app.run(debug=True)



if __name__ == "__main__":
    main()


####### JUST ADD FLASK UI TO IT AND ITS GOOD TO GO #########