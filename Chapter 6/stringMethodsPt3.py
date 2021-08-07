# join()
# join method is useful when you need to combine a list of strings into a single one
# print(', '.join(['cats','rats','bats'])) # put what you want the strings to be joined with before in quotes
# print(' '.join(['My','name','is','Simon']))
# print('ABC'.join(['My','name','is','Simon'])) # called on a string value and is passed a list value

# split()
# print('My name is Simon'.split()) # called on a string value and returns a list of strings
# by default, it splits at the space, tab, or newline characters, but the whitespace characters aren't included
# in the list returned

# delimiter string to split in a different place:
# print('MyABCnameABCisABCSimon'.split('ABC'))
# print('My name is Simon'.split('m'))

# spam = '''Dear Alice,
# How have you been? I am fine.
# There is a container in the fridge
# that is labeled "Milk Experiment."
#
# Please do not drink it.
# Sincerely,
# Bob'''
# print(spam.split('\n'))


# partition() also splits a string before and after a seperator string
# returns a tuple of three strings, the before, seperator, and after
print('Hello, world!'.partition('w'))
print('Hello, world!'.partition('world'))
print('Hello, world!'.partition('o')) # since the seperator occurs more than once, it splits by the first occurence
print('Hello, world!'.partition('XYZ'))#since the seperator cannot be found, it returns the whole string first then two empty ones
# multiple assignment trick to assign 3 returned strings to 3 variables
before, sep, after = ('Hello, world!'.partition(' '))
print(before)
print(after)
# useful for splitting a string when you need the part before, and or after a seperator