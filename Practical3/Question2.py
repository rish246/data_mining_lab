import os
import time
import csv

test_files = os.listdir('./')

output_file = 'q2_op.csv'

test_indices = [100, 200, 300, 400, 500]
time_taken = {}

start_time = time.time()

for idx, filename in enumerate(test_files):

    if filename[-1] == 'y':
        continue

    
    with open(filename, 'r+') as input_file:

        # start counting here

        file_content = input_file.read().split('\n')

        # convert Each line to uppercase
        for i in range(len(file_content)):
            file_content[i] = file_content[i].upper()

        
        # Write the File content to the output File
        # Write File content to the output file
        # Empty the contents of a file
        # The problem is my input ptr
        # place the input ptr to the starting of the file
        input_file.seek(0)

        for line in file_content:
            input_file.write(f'{line}\n')

        if (idx + 1) in test_indices:
            time_taken[idx + 1] = (time.time() - start_time)
        
    
    

# write the dict to csv file
with open(output_file, 'w', newline='') as output_file:
    writer = csv.writer(output_file)

    writer.writerows(time_taken.items())