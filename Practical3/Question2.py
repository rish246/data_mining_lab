import os
import time
import csv

test_files = os.listdir('./')

output_file = 'q2_op.csv'

test_indices = [100, 200, 300, 400, 500]
time_taken = {}

start_time = time.time()

for idx, filename in enumerate(test_files):

    if filename[-1] != 't' :
        continue

    
    with open(filename, 'r+') as input_file:


        file_content = input_file.read().split('\n')

        file_content = [string.upper() for string in file_content]

        # place the input_ptr to the start of the input file
        input_file.seek(0)

        for line in file_content:
            input_file.write(f'{line}\n')

        if (idx + 1) in test_indices:
            time_taken[idx + 1] = (time.time() - start_time)
        

    # break
    
    

# write the dict to csv file
with open(output_file, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(['Number of Files', 'Time Taken(s)'])
    writer.writerows(time_taken.items())
