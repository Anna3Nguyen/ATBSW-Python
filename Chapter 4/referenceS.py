# spam = 42
# cheese = spam
# spam = 100
# print(spam)
# print(cheese)
# integers are immutable
# spam = [0,1,2,3,4,5]
# cheese = spam # The reference is being copied, not the list
# cheese[1] = 'Hello!' # This changes the list value
# print(spam)
# print(cheese) # The cheese variable refers to the same list


# id() or unique identity function
# print(id('Howdy')) # The returned number will be different on your machine
# # return value is different each time; picks address on free bytes/space in computer
# bacon = 'Hello'
# print(id(bacon))
# bacon += ' world!'
# print(id(bacon)) # bacon now refers to a completely different string

eggs = ['cat','dog'] # This creates a new list
print(id(eggs))
eggs.append('moose') # append() modifies the list "in place"
print(id(eggs)) # eggs refers to same list as before
eggs = ['bat','rat','cow'] # This creates a new list, which has a new identity
print(id(eggs)) # eggs now refers to a completely different list