# Multiline string is used for hash comments that are really long!

"""This is a test Python program.
Written by Anna Ween @me.com

This program was designed for Python 3, not Python 2.
"""

def spam():
    """This is a multiline comment to help
    explain what the spam() function does."""
    print('Hello!')


# Indexing and Slicing STrings
spam = 'Hello, world!'
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5]) # reminder: goes up to 5 but not included
print(spam[:5])
print(spam[7:])

spam = 'Hello, world!'
fizz = spam[0:5] # slicing doesn't change the og string
print(fizz) # store the slice somewhere else in another var

# in and not in Operators (strings): works the same as normal
print('Hello' in 'Hello, World')
print('Hello' in 'Hello')
print('HELLO' in 'Hello, World')
print('' in 'spam')
print('cats' not in 'cats and dogs')
# this is case sensitive, must be exact