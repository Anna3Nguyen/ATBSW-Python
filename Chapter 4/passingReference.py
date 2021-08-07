# def eggs(someParameter):
#     someParameter.append('Hello')
#
# spam = [1,2,3]
# eggs(spam)
# print(spam) #value of arguments are copied to parameter variables; refer to same list


import copy
spam = ['A','B','C','D']
print(id(spam))
cheese = copy.copy(spam)
print(id(cheese)) # cheese is a different list with different identity
cheese[1] = 42
print(spam)
print(cheese)


