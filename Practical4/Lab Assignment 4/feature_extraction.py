# Take filenames as input args
import sys
import time
import csv
import logging
import os


def create_file(filetype):
    '''
    This function takes a filetype and create a file named base on the filetye

    @return : filename
    '''
    f_name = f'{filetype}-{time.time()}.csv'

    file_ = open(f_name, 'w')

    file_.close()

    return f_name



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

    digits_of_sequence = [char for char in seq if char.isdigit()]

    is_seq_valid = (len(digits_of_sequence) == 0)

    if not is_seq_valid:

        False, {}
    
    for char in seq:
        
        if char in resultant.keys():

            input_config[resultant[char]] += 1

    

    return True, input_config

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
    

    is_line_valid = False if (len(line) < 2) else True
    
    seq, class_ = '', ''
    
    is_class_mentioned = False


    if is_line_valid:

        seq, class_ = line.split(',')[0], line.split(',')[1]

        is_line_valid = is_class_mentioned = class_ in ['+', '-']

        class_res_values = {'+' : 1, '-' : 0}


        if is_line_valid:

            class_ = class_res_values[class_]

            is_line_valid, input_config = process_seq(seq = seq, class_=class_)

        

    if is_line_valid:
        
        return is_line_valid, input_config
    
    else:
    
        if is_class_mentioned:
    
            class_ = '-' if (class_ == 0) else '+'
        
        return is_line_valid, (seq, class_)



def process_file(filename, seq_no):
    '''
    @Input -> Filename, seq_no

    @returns -> 
        1. Updated seq_no
        2. List of Result file entries
        3. List of Log file entries

    '''

    result_entries = []

    log_entries = []

    with open(filename, 'r+') as in_file:

            file_content = in_file.read().split('\n')


            for line in file_content[1:]:
                
                is_line_valid, config = build_config(line)

                if is_line_valid:

                    config['seq_no'] = seq_no

                    new_res_entry = [config['seq_no'], config['F1'], config['F2'], config['F3'], config['F4'], config['F5'], config['F6'], config['Class']]

                    result_entries.append(new_res_entry)

                else:

                    seq, class_ = config

                    new_log_entry = [filename, seq, class_]

                    log_entries.append(new_log_entry)

                seq_no += 1
    

    return seq_no, result_entries, log_entries


def write_file(filename, entries, header):
    
    with open(filename, 'r+') as file:

        file.write(f'{header}\n')

        for entry in entries:

            # convert entry to string
            entry_str = ''

            for char in entry:
                entry_str += str(char) + ','

            file.write(entry_str[:-1] + '\n')

        file.close()



def main():
    ########## CHECK FOR WRONG PARAMS ########

    try:
        input_filenames = sys.argv[1:]

        if len(input_filenames) == 0:

            raise Exception('No file provided')

        seq_no = 1

        # result_writer, log_writer = generate_result_and_log_writer()
        result_filename = create_file(filetype='result')
        
        log_filename = create_file(filetype='log')


        result_file_entries = []

        log_file_entries = []

        
        for filename in input_filenames:

            seq_no, res_entries, log_entries = process_file(filename, seq_no=seq_no)

            result_file_entries = result_file_entries + res_entries

            log_file_entries = log_file_entries + log_entries



        # Now take the result filename
        write_file(result_filename, result_file_entries, header='Seq,F1,F2,F3,F4,F5,F6,Class')

        write_file(log_filename, log_file_entries, header='Filename,Seq,Class')

       

    except OSError as osError:

        print(f'OSError : {osError.__str__()}')

    except Exception as invalid_param_exception:

        print(f'Error : {invalid_param_exception.__str__()}')

    

                
if __name__ == "__main__":
    main()


########## ADDING UNIT TESTS AND ERROR HANDLING ################