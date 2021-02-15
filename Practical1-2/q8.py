L = ["One", "Two", "Three", "Four", "Five"]

with open("q8_output.txt", 'r+') as output_file:
    
    for item in L:
        output_file.write(f'{item}, {len(item)}\n')