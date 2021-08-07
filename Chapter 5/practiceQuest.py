# 1. What does the code for an empty dictionary look like?
{}
# 2. What does a dictionary value with a key 'foo' and a value 42 look like?
{'foo': 42}
# 3. What is the main difference between a dictionary and a list?
# list use brackets and have a integer only index and they are ordered
# dictioaries use braces can have strings or any integer for index and they are unordered and have key-value pairs
# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
# KeyError
# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# There is no difference, they do the same things
# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# 'cat' in spam checks if 'cat' is in the keys while 'cat' in spam.values() checks if its in the values of each key
# 7. What is a shortcut for the following code?
# if 'color' not in spam:
#     spam['color'] = 'black'
# spam.setdefault('color', 'black')
# 8. What module and function can be used to “pretty print” dictionary values?
# import pprint
# pprint.pprint()

