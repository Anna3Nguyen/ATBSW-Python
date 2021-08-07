# What are the two values of the Boolean data type? How do you write them?
# True and False

# What are the three Boolean operators?
# and, or, not

# Write out the truth tables of each Boolean operator
# (that is, every possible combination of Boolean values for the operator and what they evaluate to).
# True and True == True
# True and False == False
# False and True == False
# False and False == False
# True or False == True
# False or True == True
# False or False == False
# True or True == True
# not True == False
# not False == True

# What do the following expressions evaluate to?
# (5 > 4) and (3 == 5)                  False
# not (5 > 4)                           False
# (5 > 4) or (3 == 5)                   True
# not ((5 > 4) or (3 == 5))             False
# (True and True) and (True == False)   False
# (not False) or (not True)             True

# What are the six comparison operators?
# ==, !=, <, >, <=, >=

# What is the difference between the equal to operator and the assignment operator?
# The assignment operator stores a value inside a variable while the equal to operator compares to see if 2 values are the same.

# Explain what a condition is and where you would use one.
# A condition is the context of a flow control statement which evaluates to True or False.
# You would use one when your writing blocks of code.

# Identify the three blocks in this code:
# spam = 0
# if spam == 10:
#     print('eggs')
#     if spam > 5:
#         print('bacon')
#     else:
#         print('ham')
#     print('spam')
# print('spam')
# Blocks of code are inside print('eggs') and print('ham') and print('bacon)

# Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings!
# if anything else is stored in spam.

# while True:
#     print('What number is spam?')
#     spam = input()
#     if spam == '1':
#         print('Hello')
#         break
#     elif spam == '2':
#         print('Howdy')
#         break
#     else:
#         print('Greetings!')
#         break

# What keys can you press if your program is stuck in an infinite loop?
# ctrl - C

# What is the difference between break and continue?
# break stops and breaks the loop and moves on to execute the next code while continue starts back at the start of the loop.

# What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
# range(10) excutes code 10 times, range(0, 10) starts from the value 0 and doesn't inclue 10 so it goes up to 9
# range(0, 10, 1) says that it starts at zero and ends at 9 and increases by 1 but they are the same

# Write a short program that prints the numbers 1 to 10 using a for loop.
# Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# for i in range(1, 11):
#     print(i)

# i = 1
# while i < 11:
#     print(i)
#     i = i + 1

# If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# spam.bacon()