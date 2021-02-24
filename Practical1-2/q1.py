L = [11, 12, 13, 14]
print(f'Initial L = {L}\n')

# add 50 and 60 to L
# use list concat
L = L + [50, 60]
print(f'L : {L}')

# remove 11 and 13 from L
# simple list comprehension
remove_items = [11, 13]
L = [x for x in L if x not in remove_items]


# sort L in increasing order
L.sort()
print(L)
# sort in Decreasing order
L.sort(reverse=True)

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
# sum of all elements
sum_of_all_elements = sum(L)
print(f'Sum of elements of L : {sum_of_all_elements}')

# sum of odd elements
odd_elements = [element for element in L if (element % 2 != 0)]
sum_of_odd_elements = sum(odd_elements)
print(f'Sum of Odd elements : {sum_of_odd_elements}')
# sum of even elements
even_elements = [element for element in L if (element % 2 == 0)]
sum_of_even_elements = sum(even_elements)
print(f'Sum of Even Elements : {sum_of_even_elements}')

# sum of prime numbers
def is_prime(element):
    if element < 2:
        return False
    i = 2
    while i * i <= element:
        if element % i == 0:
            return False

        i += 1

    return True

prime_elements = [element for element in L if (is_prime(element))]
sum_of_prime_elements = sum(prime_elements)
print(f'Sum of Prime elements : {sum_of_prime_elements}')



# ######################################################
# ######3 Clear all elements of L
# print("CLEARED --L--")
L.clear()
# print(L)

# #######################################################
# ####3 Delete L
# print("Deleting --L--")

del L
# print(L)

print(f'L : {L}')
