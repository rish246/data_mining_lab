S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# add 55 and 66 in set 1
S1.add(55)
S1.add(66)
print(S1)

# remove 10 and 30 from s1
S1.remove(10)
S1.remove(30)
print(S1)

# check whether 40 is present in S1
print(40 in S1)


# union between S1 and S2
print ( S1 | S2 )

# intersection of two sets
print ( S1 & S2 )

# find diff bw two sets
print(S1 - S2)