import mimetypes
import sys
import smtplib
import json
import csv
import os

from email.mime.base import MIMEBase
from email.message import EmailMessage
from time import sleep

from feature_extraction import process_file, create_file, write_file

##########################################################################

def get_email_and_password(config_file_path):

    config_file = open(config_file_path)
    
    config_file_content = config_file.read()

    credentials = json.loads(config_file_content)

    MY_EMAIL = credentials['email']
    
    MY_PASSWORD = credentials['password']

    return MY_EMAIL, MY_PASSWORD


########################################################################

def construct_email_message(from_ ,to_, result_filename : str, log_filename : str) -> EmailMessage:

    msg = EmailMessage()

    msg['Subject'] = "This is the subject of new message"

    msg['From'] = from_

    msg['To'] = to_

    with open(result_filename, 'rb') as result_file:

        # send the file
        content = result_file.read()

        # # add attatchment to email
        msg.add_attachment(content, maintype='application', subtype='octet-stream', filename = result_filename)


    with open(log_filename, 'rb') as log_file:

        # send the file
        content = log_file.read()

        # # add attatchment to email
        msg.add_attachment(content, maintype='application', subtype='octet-stream', filename = log_filename)
        

    # Lets attach the result and log file

    return msg


############# Only problem left is that the files are getting deleted and do not hold any content ############## 
############ Why is it happeing ###############################################################################


def send_email(recipient_email, result_filename : str, log_filename : str):

    # Read email and password from config
    MY_EMAIL, MY_PASSWORD = get_email_and_password('config.json')

    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        # Have an smtp connection
        code, status = smtp.login(MY_EMAIL, MY_PASSWORD)

        if code == 235:
            print('Successfully logged in to google')
        
            msg = construct_email_message(MY_EMAIL, recipient_email, result_filename, log_filename)

            smtp.send_message(msg)

        smtp.close()

    #1 -> Login using your email and password

def main():

    # Take a file and an email from the command line
    try:
        if len(sys.argv) < 3:
            raise Exception('<No FILENAME or EMAIL provided>')

        filename = sys.argv[1]
        user_email = sys.argv[2]
        
        
        # print("Successfully processed files")
        result_filename = create_file(filetype='result')

        log_filename = create_file(filetype='log')

        # We created log and result files
        seq_no, res_file_entries, log_file_entries = process_file(filename, seq_no=1)



        write_file(result_filename, res_file_entries, header='Seq,F1,F2,F3,F4,F5,F6,Class')

        write_file(log_filename, log_file_entries, header='Filename,Seq,Class')


        # Send Email
        send_email(user_email, result_filename, log_filename)
        
        # if seq_no == -1:
        #     raise OSError()

    except OSError as osError:

        print(f'OSError : {osError.__str__()}')

    except Exception as invalid_param_exception:

        print(f'Error : {invalid_param_exception.__str__()}')


if __name__ == "__main__":
    main()