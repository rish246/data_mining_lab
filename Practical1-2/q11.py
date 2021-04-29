# time taken by a program
import time

def do_stuff():
    for i in range(100000):
        i = i + 3

start_time = time.time()


do_stuff()


processing_time = (time.time() - start_time)
print(f'\nTime taken by the Program : {processing_time}')

