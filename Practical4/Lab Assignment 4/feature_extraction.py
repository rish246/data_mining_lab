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

# def generate_result_and_log_writer():

#     ############## GENERATE A LOG WRITER ###############
#     log_file = create_file(filetype='log')

#     log_fieldnames = ['Filename', 'Seq', 'Class']

#     log_writer = csv.writer(log_file)

#     log_writer.writerow(log_fieldnames)


#     ################# GENERATE A RESULT WRITER ###############
#     result_file = create_file(filetype='result')

#     res_file_copy = result_file

#     result_fieldnames = ['seq_no', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'Class']

#     result_writer = csv.DictWriter(result_file, fieldnames=result_fieldnames)

#     result_writer.writeheader()

#     return result_writer, log_writer

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
                
                is_valid_line, config = build_config(line)

                if is_valid_line:

                    config['seq_no'] = seq_no

                    new_res_entry = [config['seq_no'], config['F1'], config['F1'], config['F1'], config['F1'], config['F1'], config['F1'], config['Class']]

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

        for entry in entries[1:]:

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

            original_seq_no = seq_no

            seq_no, res_entries, log_entries = process_file(filename, seq_no=seq_no)

            result_file_entries = result_file_entries + res_entries

            log_file_entries = log_file_entries + log_entries



        # Now take the result filename
        write_file(result_filename, result_file_entries, header='Seq,F1,F2,F3,F4,F5,F6,Class')

        write_file(log_filename, log_file_entries, header='Filename,Seq,Class')

        # open it in r+ mode and writethe result_file_entries to result_filename
        


            

            

        #     if seq_no == -1:

        #         seq_no = original_seq_no

        # #         # restore the original seq_number
        #         raise OSError()

                
        #     # sleep(3)

            
        # ### Get the log file and res file
        # files_in_cur_folder = os.listdir('./')
        # # print(os.path.curdir)
        # # print(files_in_cur_folder)
        # our_files = [file for file in files_in_cur_folder if (file[-4:] == '.csv')]
        
        # result_file, log_file = our_files[0], our_files[1]
        # print(result_file, log_file)
        # with open(result_file) as rf:
        #     print(rf.read())
        


                # raise an OSError

    except OSError as osError:

        print(f'OSError : {osError.__str__()}')

    except Exception as invalid_param_exception:

        print(f'Error : {invalid_param_exception.__str__()}')

    




        
                
if __name__ == "__main__":
    main()


########## ADDING UNIT TESTS AND ERROR HANDLING ################