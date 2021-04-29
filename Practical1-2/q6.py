input = [ n for n in range(100, 901) ]
# import pprint

def is_prime(element):

    if element < 2:
        return False
    i = 2
    while i * i <= element:
        if element % i == 0:
            return False

        i += 1

    return True


def is_odd(element):
    return (element % 2 != 0)

def is_even(element):
    return (element % 2 == 0)


def pretty_print(List):
    for i in range(0, len(List), 15):
        print(List[i : i + 15])

def main():
    global input

    even_numbers = [number for number in input if is_even(number)]
    odd_numbers = [number for number in input if is_odd(number)]
    prime_numbers = [number for number in input if is_prime(number)]

    sum_odd = sum(odd_numbers)
    sum_even = sum(even_numbers)
    sum_prime = sum(prime_numbers)
        
    # print('Odd numbers')
    # pretty_print(odd_numbers)
    # print(f'Sum of odd numbers {sum_odd}')

    # print('Even Numbers')
    # # print(even_numbers)
    # pretty_print(even_numbers)
    # print(f'Sum of Even Numbers : {sum_even}')

    print('Prime Numbers')
    # print(prime_numbers)
    pretty_print(prime_numbers)
    print(f'Sum of Prime numbers : {sum_prime}')

main()