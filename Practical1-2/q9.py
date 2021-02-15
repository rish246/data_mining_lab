# generate 100 random strings len in range(10, 15) -> file
import string
import random

range_start, range_end = 10, 16

n_strings = 100

letters = string.ascii_letters

with open('q9_output.txt', 'r+') as output_file:

    for i_string in range(n_strings):

        # generate a string 
        len_random_str = random.randint(range_start, range_end)

        random_str = ''.join(random.choice(letters) for i in range(len_random_str))

        # write string to file
        output_file.write(f'{random_str}\n')