# print("First R program");


# # select and run
# ############ Vector operation
# my.vector <- c(1, 3, 2);

# # add 1 to each term of R
# my.vector <- my.vector + 1;

# # substract 1 from each element of my.vector
# my.vector <- my.vector - 1;

# # check if division and muliplication works too
# my.vector <- my.vector / 2;

# my.vector <- my.vector * 3;

# # get the mean value of the vector

# print(my.vector);




# ################### Creating some useful vectors in R #############
# ##### using : operator
# first.fifty.natural.numbers <- 1:50;

# print(first.fifty.natural.numbers);


# #############3 count from 100 to 1 in reverse #########3
# reverse.counting <- 100:1;

# print(reverse.counting);


# ###########3 using seq function
# # syntax : seq(from, to, [by | length ])
# # can only has 3 args
# first.ten.multiples.of.two <- seq(2, 100, by = 2);

# print(first.ten.multiples.of.two);

# # rep function.. repeat the input vector over and over
# # print(rep(reverse.counting, 3)); 
# # Define length of the output
# print(rep(reverse.counting, out.length = 60));


# Exercise 2.3. Create the following vectors in R using seq() and rep().

# 1
# .
# P
# (v) 1, 3, 6, 10, 15, . . . , ni=1 i, . . . , 210 [look up ?cumsum].
# (vi)
# ∗
# 1, 2, 2, 3, 3, 3, 4, . . . , 9, 10, . . . , 10 . [Hint: type ?seq, and read about
# | {z }
# 1

# (i) 1, 1.5, 2, 2.5, . . . , 12
first.vector <- seq(1, 12, by = 0.5);
print(first.vector);


# (ii) 1, 8, 27, 64, . . . , 1000.
# second.vector <- (1:10) ^ 3;
# print(second.vector);

# use recycling instead
second.vector <- seq(1, 10);

# add these vectors one after other
second.vector <- second.vector * second.vector * second.vector;

# vector1 * vector2 => for i in range(lenVectors) : result[i] = (vector1[i] * vector2[i]);



print(second.vector);

########################################
# (iii) 1, −1/2, 1/3, -1/4, . . . , − 1/100
third.vector <- seq(1, 100, length = 100);

div.vector <- c(1, -1);
# divide by 1
third.vector <- div.vector / third.vector;

print(third.vector);


############################################
# (iv) 1, 0, 3, 0, 5, 0, 7, . . . , 0, 49.

forth.vector <- seq(1, 49);

mul.vector <- c(1, 0);

forth.vector <- mul.vector * forth.vector;

print(forth.vector);

##############################################
# cumsum algorithm
fifth.vector <- cumsum(1:210);
print(fifth.vector);

##################333 
# last vector
# 1, 2, 2, 3, 3, 3, 4, . . . , 9, 10, . . . , 10 . [Hint: type ?seq, and read about