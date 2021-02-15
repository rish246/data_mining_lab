range_start, range_end = 1, 100

from q6 import is_prime


with open('q10_output.txt', 'r+') as output_file:
    for number in range(range_start, range_end):
        if is_prime(number):
            output_file.write(f'{number}\n')
