L = [11, 12, 13, 14]

# add 50 and 60 to L
# use list concat
L = L + [50, 60]
print(L)

# remove 11 and 13 from L
# simple list comprehension
remove_items = [11, 13]
L = [x for x in L if x not in remove_items]
print(L)

# sort L in increasing order
# use simple bubble sort

# sort in Decreasing order
def swap(List, first_idx, second_idx):
    # since lists are passed by ref... hence any changes here will change final op
    temp = List[first_idx]
    List[first_idx] = List[second_idx]
    List[second_idx] = temp

def sort(List, compare, mode):
    i_round = 1
    while i_round < len(List):
        cur_idx = 0
        while cur_idx < (len(List) - 1):
            
            if compare(List[cur_idx], List[cur_idx + 1], mode):
                swap(List, cur_idx, cur_idx + 1)
            cur_idx += 1

        i_round += 1

# pass comparison lambda
INCREASING_ORDER = 0
DECREASING_ORDER = 1

def compare(firstEl, secondEl, mode):
        if(mode == INCREASING_ORDER):
            return firstEl > secondEl
        else:
            return firstEl < secondEl

def sort_L():
    global L

    sort(L, compare, INCREASING_ORDER)
    print(f'Ascending order L : {L}')


    sort(L, compare, DECREASING_ORDER)
    print(f'Descending order L : {L}')

sort_L()


################################################
# search 13 in L
def search(List, element):
    return ( element in List)

print(f'IS 13 PRESENT IN L : {search(L, 13)}')


##################################################3
def count_elements(List):
    return len(List)

print(f'NUMBER OF ELEMENTS IN L: {count_elements(L)}')

##################################################
ALL = 0
ODD = 1
EVEN = 2
PRIME = 3

def is_prime(element):
    i = 2
    while i * i <= element:
        if element % i == 0:
            return False

        i += 1

    return True


def is_right(element, mode):
    if mode != ALL:
        if mode == EVEN:
            return (element % 2 == 0)
        elif mode == ODD:
            return (element % 2 != 0)
        else:
            return is_prime(element)

    else:
        return True

def sum_elements(List, comparison_func, mode = ALL):
    sum = 0
    for element in List:
        if(comparison_func(element, mode)):
            sum += element
    return sum

print(f'SUM OF ALL ELEMENTS OF L: { sum_elements(L, is_right)} ')

print(f'SUM OF ALL THE ODD ELEMENTS OF L : {sum_elements(L, is_right, ODD)}')

print(f'SUM OF ALL EVEN ELEMENTS OF L: {sum_elements(L, is_right, EVEN)}')

print(f'SUM OF ALL THE PRIME NUMBERS OF L: { sum_elements(L, is_right, PRIME) }')


######################################################
######3 Clear all elements of L
print("CLEARED --L--")
L.clear()
print(L)

#######################################################
####3 Delete L
print("Deleting --L--")

del L
print(L)