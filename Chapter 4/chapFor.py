# spam[1] = 'aardvark' means “Assign the value at index 1 in the list spam to the string 'aardvark'.”
# spam = ['cat', 'bat', 'rat', 'elephant']
# spam[1] = 'aardvark'
# print (spam)
# spam[2] = spam[1]
# print (spam)
# spam[-1] = 12345
# print (spam)


# + combines two lists into one list and * can be used to replicate a list a certain amount of times
# print ([1, 2, 3]+['A', 'B', 'C'])
# print (['X', 'Y', 'Z']*3)
# spam = [1, 2, 3]
# spam = spam + ['A', 'B', 'C']
# print (spam)


# the del statement deletes values at an index in the list; all values after the deleted value move up 1 index
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print (spam)
del spam[2]
print (spam)
# You can also use the del statement to delete variables, but most times values are deleted


