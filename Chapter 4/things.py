# the things that you can do with lists can also be done with other data types
# name = ('Zophie')
# print(name[0])
# print(name[-2])
# print(name[0:4])
# print('Zo' in name)
# print('z' in name)
# print('p' not in name)
# for i in name:
#     print('*** '+i+' ***')


# a list value is a mutable data type meaning it can have values added removed or changed
# strings are immutable meaning it can't be changed
# TypeError
# name = 'Zophie a cat'
# name[7] = 'the'
# To change a string properly, use slicing or concatenation to build a new string
# name = 'Zophie a cat'
# newName = name[0:7] + 'the' + name[8:12]
# print(name) # old bucket/variable
# print(newName) # new bucket/variable

# eggs = [1,2,3]
# eggs = [4,5,6] # does not add or modify to eggs but it is being overwritten
# print(eggs)
# to add and modify the original list:
# eggs = [1,2,3]
# del eggs[2]
# del eggs[1]
# del eggs[0]
# eggs.append(4)
# eggs.append(5)
# eggs.append(6)
# print(eggs)


# tuple data type is identical to lists, but they are typed with () instead and are immutable
# eggs = ('hello', 42, 0.5)
# print(eggs[0])
# print(eggs[1:3])
# print(len(eggs))
# # TypeError:
# # eggs[1] = 99
# # If you only have 1 value in your tuple, place a trailing comma so Python knows its a tuple data type
# print(type(('hello',)))
# print(type(('hello')))


# list() and tuple() Functions
print(tuple(['cat','dog',5]))
print(list(('cat','dog',5))) # put double ()s because of 2 arguments? yes probably
print(list('hello'))


