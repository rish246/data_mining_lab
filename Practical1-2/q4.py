######## generate 100 random strings with length 6 and 8 #####
import string
import random

length_options = [6, 7, 8]

letters = string.ascii_letters

hundred_random_strings = []
# make random perms of letters
for i_str in range(0, 100):
    random_len = random.choice(length_options)
    random_string = ''.join(random.choice(letters) for i in range(random_len))

    hundred_random_strings.append(random_string)

print(len(hundred_random_strings))
print(hundred_random_strings)



#####################################################################
######3 print prime numbers bw 600 and 800
is_prime = [1 for i in range(801)]

# 0 and 1 are not prime
is_prime[0] = is_prime[1] = 0

# use sieve
i_element = 2
while (i_element ** 2) <= 800:
    if is_prime[i_element]:
        # mark its multiples as not prme
        for j_element in range(i_element ** 2, 801, i_element):
            is_prime[j_element] = 0

    i_element += 1

our_range = [2, 100]
prime_nums_in_our_range = [n for n in range(our_range[0], our_range[1]) if is_prime[n]]
print(prime_nums_in_our_range) 



###########################################################################
nums_divisible_by_7_or_9 = [n for n in range(100, 1001) if(n % 63 == 0)]
print(nums_divisible_by_7_or_9)