import random

range_start, range_end = 10, 31

numbers = [n for n in range(range_start, range_end)]

list_one = [random.choice(numbers) for i in range(10)]

list_two = [random.choice(numbers) for i in range(10)]

print('\n')
print(f'List One : {list_one}')
print(f'List Two : {list_two}')


#######################################
#####3 Common numbers in two lists
# common_elements = [n for n in list_one if n in list_two]
# print(f'Common Elements : {common_elements}')


##########################################
# ## unique number in both lists
# unique_elements_list_one = [ n for n in list_one if n not in list_two]
# unique_elements_list_two = [ n for n in list_two if n not in list_one]

# unique_elements = unique_elements_list_one + unique_elements_list_two
# print(f'\nUnique elements in A and B : {unique_elements}')

# ######################################################################
# #3 min in both the list
min_list_one = min(list_one)
min_list_two = min(list_two)

min_value_across_both_lists = min(min_list_one, min_list_two)

# ########################################################################3
max_list_one = max(list_one)
max_list_two = max(list_two)

max_value_across_both_lists = max(max_list_one, max_list_two)
# print(f'Maximum value across both lists : {max_value_across_both_lists}')


# #####################################################################
# ######### sum of both lists
sum_list_one = sum(list_one)
sum_list_two = sum(list_two)
total_sum = sum_list_one + sum_list_two
print(f'Sum of Values of both lists : {total_sum}')


# print(list_one)

# print(list_two)

# print(common_elements)

# print(unique_elements_list_one)
# print(unique_elements_list_two)
# print(unique_elements)

# print(min_value_across_both_lists)
# print(max_value_across_both_lists)
# print(total_sum)