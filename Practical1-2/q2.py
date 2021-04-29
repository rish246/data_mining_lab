# dictionaries
import json

D = { 
    1 : 5.6,
    2 : 7.8, 
    3 : 6.6, 
    4 : 8.7, 
    5 : 7.7
}
print('Original D : ')
print(json.dumps(D, indent=2))


# remove key 2
del D[2]


print(D)

# if 6 is present in D
is_6_present = ( 6 in D)
print(f'Is 6 present in D : {is_6_present}')

# count number of elements in D
print(f'\nNumber of Elements in D = {len(D)}')

print(D)

# add the values of D
sum_values = sum(D.values())

print(f'\nSum of Values in D : {sum_values}')


# update value of 3 in D
D[3] = 7.1
D.clear()

# print(D)
print('\n\n')
# add { 8 : 8.8 } in D
print('D after operation : ')
# D[8] = 8.8
print(json.dumps(D, indent=2))


# # clear D
# print(D)