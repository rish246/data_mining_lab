# Take filenames as input args
import sys

def process_seq(resultant, line_no, input_config, seq):

    is_valid_line = True
    
    for char in seq:
        if char in resultant.keys():

            input_config[resultant[char]] += 1


        elif char.isdigit() or char in ['+', '-']:
            # Write this in the log file
            is_valid_line = False

            break

    return is_valid_line, input_config

def build_config(line, resultant, line_no):
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

    if is_valid_line:

        seq = line.split(',')[0]

        class_ = line.split(',')[1]

        if class_ not in ['+', '-']:
            is_valid_line = False

        if is_valid_line:
            is_valid_line, input_config = process_seq(seq = seq, line_no=line_no, resultant=resultant, input_config=input_config)

        

    if is_valid_line:
        return is_valid_line, input_config
    else:
        return is_valid_line, {}



def process_file(filename, seq_no):
    '''
    @Input -> Filename

    @what -> This function takes filename as input
                read each line in the file
                if line is ok -> write it in the result file
                else -> Create an entry in the log file

    '''
    line_no = 0
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



            for line, line_no in enumerate(file_content[1:]):
                
                is_valid_line, config = build_config(line, resultant, line_no)

                if is_valid_line:
                    # print(config)
                    pass
                else:
                    print(f'Write an entry in the log file for Line {line}')

                





def main():

    input_filenames = sys.argv[1:]

    seq_no = 1

    for filename in input_filenames:

        process_file(filename, seq_no)

        break

        
                

                




if __name__ == "__main__":
    main()