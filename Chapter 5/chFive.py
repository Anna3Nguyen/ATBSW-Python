# a dictionary is a mutable collection of values; its index can use many different data types, not just ints
# Dictionary indexes are called keys, which with its associated value is called a key-value pair
# Dictionary are typed with the fancy brackets called braces { }
# myCat = {'size':'fat', 'color': 'gray', 'disposition':'loud'}
# print(myCat['size'])
# print('My cat has '+ myCat['color']+ ' fur.')  # type in keys with regular brackets []
# # Dictionaries can use ints as keys but they don't have to start at zero; they can be any #
# spam = {12345: 'Luggage Combination', 42: 'The Answer'}

# order matters when determining if two lists are the same
# spam = ['cats','dogs','moose']
# bacon = ['dogs','moose','cats']
# print(spam == bacon)
# dictionaries are unorderec so it doesn't matter what order its typed in
# eggs = {'name': 'Zophie','species': 'cat','age': '8'}
# ham = {'species': 'cat','age': '8','name': 'Zophie'}
# print(eggs == ham)
# since dictionaries are ordered they can't be sliced

# KeyError (when you try to access a key that doesn't exist)
# spam = {'name': 'Zophie','age': 7}
# print(spam['color'])


# Ordered dictionaries in Python 3.7 remember insertion order if you create a sequence value for it
eggs = {'name': 'Zopbie', 'species': 'cat', 'age': '8'}
print(list(eggs))
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(list(ham))

# Python 3.5 will not match insertion
spam = {}
spam['first key'] = 'value'
spam['second key'] = 'value'
spam['third key'] = 'value'
print(list(spam)) # may or may not match
