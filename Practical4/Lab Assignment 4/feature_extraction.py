# Take filenames as input args
import sys

def main():

    input_filenames = sys.argv[1:]

    seq_no = 1

    for filename in input_filenames:
        
        
        # Open the file and read the content
        with open(filename, 'r+') as in_file:

            line_no = 1
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
                print(line)
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

                

                # Line -> seq, Class
                    seq = line.split(',')[0]

                    class_ = line.split(',')[1]

                    for char in seq:

                        # FIll the config
                        if char in resultant.keys():
                            print(f'{char}, {resultant[char]}\n')

                            input_config[resultant[char]] += 1

                        # IF CHAR is digit
                        # Go to the next line
                        elif char.isdigit() or char in ['+', '-']:
                            # Write this in the log file
                            print(f'Invalid seq {seq} at line number {line_no}\n')

                            is_valid_line = False

                            break



                if is_valid_line:
                    print(input_config)
                else:
                    print('Write an entry in the log file')



                # Write input config to the resultant file
                # FOR NOW JUST WRITE THE LINE--> REFACTOR LATER
                
            break


                    # Char is valid



        line_no += 1
                

                




if __name__ == "__main__":
    main()