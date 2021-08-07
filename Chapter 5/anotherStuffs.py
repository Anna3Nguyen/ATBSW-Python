# spam = {'name': 'Zophie', 'age': 7}
# print('name' in spam.keys())
# print('Zophie' in spam.values())
# print('color' in spam.keys())
# print('color' not in spam.keys())
# print('color' in spam) #shorter version of writing 'color' in spam.keys()/ works on a dict keys

#get() method takes two arguments: the key of the value to retrieve and a fallback value to return if that key does not exist.
# picnicItems = {'apples': 5, 'cups': 2}
# print('I am bringing ' + str(picnicItems.get('cups', 0))+ ' cups.')
# print('I am bringing ' + str(picnicItems.get('eggs', 0))+' eggs.')
# Error:
# print('I am bringing ' + str(picnicItems['eggs'])+' eggs')


# setdefault() method
# spam = {'name': 'Pooka', 'age': 5}
# if 'color' not in spam:
#     spam['color'] = 'black'
# one line setdefault() code: first argument passed to the method is the key to check for,
# and the second argument is the value to set at that key if the key does not exist.
# if the key exists, the method returns its value
spam = {'name': 'Pooka', 'age': 5}
print(spam.setdefault('color', 'black'))
print(spam)
print(spam.setdefault('color', 'white'))
print(spam)