input = [ n for n in range(1, 10) ]


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


def main():
    global input


    sum_odd = 0
    sum_even = 0
    sum_prime = 0
    
    print(input)
    for number in input:
        if is_even(number):
            sum_even += number

        if is_odd(number):
            sum_odd += number

        if is_prime(number):
            sum_prime += number

        
    print(sum_odd)
    print(sum_even)
    print(sum_prime)

main()