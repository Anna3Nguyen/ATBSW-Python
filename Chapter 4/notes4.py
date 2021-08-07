# for i in range(4):
#     print(i)
#
# for i in [0, 1, 2, 3]:
#     print(i)
#
# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for i in range(len(supplies)):
#     print('Index '+str(i)+' in supplies is: '+ supplies[i])

# A common Python technique is to use range(len(someList)) with a for loop to repeat over the indexes of a list
# Like other operators, in and not in are used in expressions and connect two values:
#  a value to look for in a list and the list where it may be found. These expressions will evaluate to a Boolean value.

print ('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)
print('howdy' not in spam)
print('cat' not in spam)