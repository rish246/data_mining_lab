D = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five"
}


with open('q7_output.txt', 'r+') as output_file:

    for key, value in D.items():
        output_file.write(f'{value}, {len(value)}\n')

