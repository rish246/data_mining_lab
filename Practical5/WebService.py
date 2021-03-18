import smtplib
import json

from email.message import EmailMessage


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

def get_user_input():
    input_filename = "./Lab Assignment 05/Input files for Assignment05/data.csv" 
    weights = [1, 1, 1, 2] 
    impacts = ['+','+','-','+']
    user_email = "rishabhkatna2228@gmail.com"

    # extract data 
    input_data = open(input_filename).read().strip('\n').split('\n')
    return input_data, weights, impacts, user_email

def main():

    # Take a file and an email from the command line
    input_data, weights, impacts, user_email = get_user_input()

    input_data_copy = input_data.copy()

    input_matrix = generate_matrix(input_data)

    output_filename = 'output.csv'

    performance_score, ranks = apply_TOPSIS(input_matrix, weights, impacts)

    write_result_in_output_file(input_data_copy, performance_score, ranks, output_filename)


    # use input_matrix to generate  output_file
    send_email(user_email, output_filename)


    print(input_matrix)


if __name__ == "__main__":
    main()


####### JUST ADD FLASK UI TO IT AND ITS GOOD TO GO #########