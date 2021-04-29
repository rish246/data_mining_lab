import random
import time

def generate_random_list(size):
    return [random.randint(1, 100000) for i in range(size)]


def write_result(list_sizes, exec_times):
    with open('q13_output.txt', 'r+') as output_file:
        output_file.write('List Size\tExecution Time(ns)\n')

        for index, size in enumerate(list_sizes):
            output_file.write(f'{size}\t{exec_times[index]}\n')


def main():
    list_sizes = [5000, 10000, 15000, 20000, 25000]

    exec_times = []
    for size in list_sizes:

        # generate a list of size
        random_list = generate_random_list(size)

        start_time = time.time()

        random_list.sort()

        exec_times.append((time.time() - start_time) * 1000)



    write_result(list_sizes, exec_times)

main()