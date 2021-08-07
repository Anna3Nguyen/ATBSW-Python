# -1 is the last index in a list and -2 is the second to last index in a list

# spam = ['cat', 'bat', 'rat', 'elephant']
# print (spam[-1])
# print (spam[-3])
# print ('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')


# a slice can get several values from a list in the form of a new list
# it is typed between [] and has 2 integers seperated by a colon
# example: spam[1:4]
# the first integer is where the slice starts, the second integer is where it ends
# it goes up to but does not include the value of the 2nd index

# spam = ['cat', 'bat', 'rat', 'elephant']
# print (spam[0:4])
# print (spam[1:3])
# print (spam[0:-1])
# Leaving out the 1st index is the same as using 0 or start of the list
# Leaving out the 2nd index is the same as using the length of the list, which slices to the end of the list
# print (spam[:2])
# print (spam[1:])
# print (spam[:])

# The len() function returns the number of values that are in the list value passed to it

spam = ['cat', 'dog', 'moose']
print (len(spam))
