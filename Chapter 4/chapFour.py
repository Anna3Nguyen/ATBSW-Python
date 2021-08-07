# A list is a value that contains multiple values in an ordered sequence.
# The term list value refers to the list itself (which is a value that can be stored in a variable or passed to a function
# like any other value), not the values inside the list value.
# Lists are enclosed in []s
# Values inside lists are items, which are seperated by commas (comma-delimited)

# print([1, 2, 3])
# print(['cat', 'bat', 'rat','elephant'])
# print(['hello',3.1415,True,None,42])
# spam = ['cat', 'bat', 'rat', 'elephant']
# print (spam)

# The value [] is an empty list that contains no values like '', and empty string



# The integer inside the [] that follows the list is called an index
# The first value of the index is 0, the 2nd is 1, the 3rd is 2, and so on

# spam = ['cat','bat','rat','elephant']
# print (spam[0])
# print (spam[1])
# print (spam[2])
# print (spam[3])
# print (['cat','bat','rat','elephant'][3])
# print ('Hello,'+ spam[0])
# print ('The ' + spam[1] + ' ate the ' + spam[0])

#Error (IndexError):
# spam = ['cat', 'bat', 'rat', 'elephant']
# print (spam[10000])

#Indexes can only be integer values, not floats, if you enter a float, you will be given a TypeError

# spam = ['cat', 'bat', 'rat', 'elephant']
# print (spam[1])
# print (spam[1.0])
# print (spam[int(1.0)])

# Lists can also contain other list values

spam = [['cat','bat'],[10, 20, 30, 40, 50]]
#       list value 0     list value 1
print (spam[0])
print (spam[0][1])
print (spam[1][4])
# The first index says which list value to use, the second index says which value within the list value
# If you use only one index, the program will print the full list
