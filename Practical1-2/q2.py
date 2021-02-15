# dictionaries
D = { 
    1 : 5.6,
    2 : 7.8, 
    3 : 6.6, 
    4 : 8.7, 
    5 : 7.7
}

# add { 8 : 8.8 } in D
D[8] = 8.8
print(D)

# remove key 2
del D[2]
print(D)

# if 6 is present in D
is_6_present = ( 6 in D)
print(is_6_present)

# count number of elements in D
print(len(D))

print(D)

# add the values of D
sum_values = 0
for value in D.values():
    sum_values += value

print(sum_values)


# update value of 3 in D
D[3] = 7.1
print(D)


# clear D
D.clear()
print(D)