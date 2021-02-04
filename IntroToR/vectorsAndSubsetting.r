#############3 Learn about operations that can be performed on vectors in R

my.vector <- c(1:100)
# single value
# R indices start from 1 rather than 0
tenth.value <- my.vector[1];
print(tenth.value);

# range of values
first.ten.values <- my.vector[1:10]
print(first.ten.values);

# random values based on a vector of indices
random.index.vector <- c(1, 3, 2, 10, 45);
random.index.values <- my.vector[random.index.vector];

print(random.index.values);


# Exercise 2.5. The built-in vector LETTERS contains the uppercase letters
# of the alphabet. Produce a vector of (i) the first 12 letters; (ii) the odd
# ‘numbered’ letters; (iii) the (English) consonants.

# Ex: 2.5
print(LETTERS);

# 1st 12 letters
first.twelve.letters <- LETTERS[1:12];
print(first.twelve.letters);

# Odd numbered letters
odd.numbered.indices <- seq(1, 26, by = 2);
odd.index.letters <- LETTERS[odd.numbered.indices];

print(odd.index.letters);

# English consonants
# - sign before index -> do not consider the index with - sign
vowels.indices <- c(1, 5, 9, 15, 21);
consonants <- LETTERS[-vowels.indices];
print(consonants);