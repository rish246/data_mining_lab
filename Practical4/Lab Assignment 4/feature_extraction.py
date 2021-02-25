# Take filenames as input args
import sys
import time
import csv

def process_seq(resultant, input_config, seq):

    is_valid_line = True
    
    for char in seq:
        if char in resultant.keys():

            input_config[resultant[char]] += 1


        elif char.isdigit() or char in ['+', '-']:
            # Write this in the log file
            is_valid_line = False

            break

    return is_valid_line, input_config

def build_config(line, resultant):
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
    input_config = {
        'F1' : 0,
        'F2' : 0,
        'F3' : 0,
        'F4' : 0,
        'F5' : 0,
        'F6' : 0,
        'Class' : 0

    }

    is_valid_line = True

    ## class and sequence should be valid
    if len(line) < 2:
        is_valid_line = False

    seq = ''
    class_ = ''
    no_class_found = False


    if is_valid_line:

        seq = line.split(',')[0]

        class_ = line.split(',')[1]


        if class_ not in ['+', '-']:
            is_valid_line = False 
            no_class_found = True
        else:
            class_ = 1 if class_ == '+' else 0


    

        input_config['Class'] = class_

        if is_valid_line:
            is_valid_line, input_config = process_seq(seq = seq, resultant=resultant, input_config=input_config)

        

    if is_valid_line:
        return is_valid_line, input_config
    else:
        if no_class_found:
            class_ = ''
        else:
            class_ = '-' if (class_ == 1) else '+'
        
        return is_valid_line, (seq, class_)



def process_file(filename, seq_no, result_file_writer_obj, log_file_writer_obj):
    '''
    @Input -> Filename

    @what -> This function takes filename as input
                read each line in the file
                if line is ok -> write it in the result file
                else -> Create an entry in the log file

    '''
    with open(filename, 'r+') as in_file:

            file_content = in_file.read().split('\n')

            resultant = {
                'N' : 'F1',
                'H' : 'F2',
                'Q' : 'F3',
                'G' : 'F4',
                'D' : 'F5',
                'T' : 'F6'

            }



            for line in file_content[1:]:
                
                is_valid_line, config = build_config(line, resultant)

                if is_valid_line:
                    config['seq_no'] = seq_no
                    seq_no += 1

                    # print(config)
                    result_file_writer_obj.writerow(config)

                else:
                    seq, class_ = config
                    
                    log_file_writer_obj.writerow([filename, seq, class_])

    return seq_no





def main():

    input_filenames = sys.argv[1:]

    seq_no = 1

    # Create a result file
    # This will create a new file
    res_time = time.time()

    result_file = open(f'result-{res_time}.csv', 'w')

    result_file.close()

    result_file = open(f'result-{res_time}.csv', 'a')


    # Construct a similar log file
    log_time = time.time()

    log_file = open(f'log-{log_time}.csv', 'w')

    log_file.close()

    log_file = open(f'log-{log_time}.csv', 'a')


    # Open the file in append mode now

    input_fieldnames = ['seq_no', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'Class']

    log_fieldnames = ['Filename', 'Seq', 'Class']

    log_writer = csv.writer(log_file)

    log_writer.writerow(log_fieldnames)

    writer = csv.DictWriter(result_file, fieldnames=input_fieldnames)

    # Write the header to the result file
    writer.writeheader()


    for filename in input_filenames:

        # For each file, we are going to write rows in the result file
        print(filename)

        seq_no = process_file(filename, seq_no, writer, log_writer)



        
                

                




if __name__ == "__main__":
    main()