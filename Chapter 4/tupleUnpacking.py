# instead of:
# cat = ['fat', 'gray', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]
# you could do:
# cat = ['fat', 'gray', 'loud']
# size, color, disposition, = cat
# if the number of variables and the length of the list don't match, Python gives a ValueError



# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for index, item in enumerate(supplies):
#     print('Index '+str(index)+ ' in supplies is: '+ item)

# enumerate() will return two values: the index of the item in the list, and the item in the list itself.



# import random
# pets = ['Dog', 'Cat', 'Moose']
# print(random.choices(pets))
# print(random.choices(pets))
# print(random.choices(pets))

# import random
# people = ['Alice', 'Bob', 'Carol', 'David']
# random.shuffle(people)
# print(people)


# spam = 42
# spam = spam + 1
# print(spam)
# # or:
# spam = 42
# spam += 1
# print (spam)

# spam +-*/%=1 is the same as spam = spam (operator) 1

spam = 'Hello'
spam += ' world!'
print(spam)
bacon = ['Zophie']
bacon *= 3
print(bacon)