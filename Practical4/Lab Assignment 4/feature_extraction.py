# Take filenames as input args
import sys
import time
import csv
import logging


def create_and_open_file(filetype):
    f_time = time.time()

    file_ = open(f'{filetype}-{f_time}.csv', 'w')

    file_.close()

    file_ = open(f'{filetype}-{f_time}.csv', 'a')


    return file_

def generate_result_and_log_writer():

    ############## GENERATE A LOG WRITER ###############
    log_file = create_and_open_file(filetype='log')

    log_fieldnames = ['Filename', 'Seq', 'Class']

    log_writer = csv.writer(log_file)

    log_writer.writerow(log_fieldnames)


    ################# GENERATE A RESULT WRITER ###############
    result_file = create_and_open_file(filetype='result')

    result_fieldnames = ['seq_no', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'Class']

    result_writer = csv.DictWriter(result_file, fieldnames=result_fieldnames)

    result_writer.writeheader()

    return result_writer, log_writer

def process_seq(class_, seq):

    input_config = {
        'F1' : 0,
        'F2' : 0,
        'F3' : 0,
        'F4' : 0,
        'F5' : 0,
        'F6' : 0,
        'Class' : 0

    }

    resultant = {
                'N' : 'F1',
                'H' : 'F2',
                'Q' : 'F3',
                'G' : 'F4',
                'D' : 'F5',
                'T' : 'F6'

            }

    input_config['Class'] = class_


    is_valid_line = True
    
    for char in seq:
        
        if char in resultant.keys():

            input_config[resultant[char]] += 1

        elif char.isdigit() or char in ['+', '-']:
            # Write this in the log file
            is_valid_line = False

            break

    return is_valid_line, input_config

def build_config(line):
    '''
    @What -> This function takes a line from file as an input
                Check if the line is valid

                A line is valid if --> 1) It has 2 columns
                                        No digit in first column
                                        +/- in second column

                if Line is valid, build a config and return
                else 
                    return {} and Invalid line
    '''
    

    is_valid_line = False if (len(line) < 2) else True
    
    seq, class_ = '', ''
    
    no_class_found = False


    if is_valid_line:

        seq, class_ = line.split(',')[0], line.split(',')[1]


        if class_ not in ['+', '-']:

            is_valid_line = False 

            no_class_found = True

        else:

            class_ = 1 if class_ == '+' else 0


        if is_valid_line:

            is_valid_line, input_config = process_seq(seq = seq, class_=class_)

        

    if is_valid_line:
        
        return is_valid_line, input_config
    
    else:
    
        if no_class_found:
    
            class_ = ''
    
        else:
    
            class_ = '-' if (class_ == 1) else '+'
        
        return is_valid_line, (seq, class_)



def process_file(filename, result_file_writer_obj, log_file_writer_obj, seq_no):
    '''
    @Input -> Filename

    @what -> This function takes filename as input
                read each line in the file
                if line is ok -> write it in the result file
                else -> Create an entry in the log file

    '''
    try:
        with open(filename, 'r+') as in_file:

                file_content = in_file.read().split('\n')


                for line in file_content[1:]:
                    
                    is_valid_line, config = build_config(line)

                    if is_valid_line:

                        config['seq_no'] = seq_no

                        

                        result_file_writer_obj.writerow(config)

                    else:

                        seq, class_ = config

                        log_file_writer_obj.writerow([filename, seq, class_])

                    seq_no += 1
    except OSError:

        return -1

    return seq_no





def main():
    ########## CHECK FOR WRONG PARAMS ########

    try:
        input_filenames = sys.argv[1:]

        if len(input_filenames) == 0:

            raise Exception('No file provided')

        seq_no = 1

        result_writer, log_writer = generate_result_and_log_writer()


        for filename in input_filenames:

            original_seq_no = seq_no

            seq_no = process_file(filename, result_writer, log_writer, seq_no=seq_no)

            if seq_no == -1:

                seq_no = original_seq_no

                # restore the original seq_number
                raise OSError()

                # raise an OSError

    except OSError:

        print(f'File not found : Can\'t open file : {filename}.. Please provide a valid filename')

    except Exception as invalid_param_exception:

        print(f'Error : {invalid_param_exception.args[0]}... please provide a file path through the command line arg')

    




        
                
if __name__ == "__main__":
    main()


########## ADDING UNIT TESTS AND ERROR HANDLING ################