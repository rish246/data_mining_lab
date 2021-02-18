# create 500 files
import string
import random

n_files = 500
n_lines = 20000
str_size = 20

letters = string.ascii_letters

for i_file in range(n_files):

    # create new file
    with open(f'{i_file + 1}.txt', 'w') as output_file:
        
        # write 20,000 lines
        for i_line in range(n_lines):
            
            # create a random string of size 20
            random_string = ''.join(random.choice(letters) for i in range(str_size))

            output_file.write(f'{random_string}\n')
            


# create 500 files

# create 500 files

# create 500 files

# create 500 files


