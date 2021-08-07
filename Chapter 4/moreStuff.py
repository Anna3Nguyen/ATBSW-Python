# spam = ['cat','bat','rat','elephant']
# spam.remove('bat')
# print(spam)
# If you delete something thats not in the list you get a ValueError
# spam = ['cat','bat','rat','elephant']
# spam.remove('chicken')

# If the value appears many times on the list, only the first instance of the value is removed
# spam = ['cat','bat','rat','cat','hat','cat']
# spam.remove('cat')
# print(spam)
#The del statement is good to use when you know the index of the value you want to remove from the list.
# The remove() method is useful when you know the value you want to remove from the list.


# sort() Method
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print (spam)
spam = ['ants','cats','dogs','badgers','elephants']
spam.sort()
print(spam)
# If you want to reverse the order, do this:
spam.sort(reverse=True)
print(spam)
# you cannot sort lists that have both number values and string values in them; you get TypeError if you do
# TypeError
# spam = [1,3,2,4,'Alice','Bob']
# spam.sort()
# sort() uses “ASCIIbetical order” rather than actual alphabetical order for sorting strings.
# This means uppercase letters come before lowercase letters.
spam = ['Alice','ants','Bob','badgers','Carol','cats']
spam.sort()
print(spam)
# If you need to sort by regular alphab. order, do str.lower for the key keyword argument
spam =['a','z','A','Z']
spam.sort(key=str.lower)
print(spam)
# This makes it treat all the items like lowercase without changing the value