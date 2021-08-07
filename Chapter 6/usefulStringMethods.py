# upper() ; lower()
# return a new string where the string is turned into an uppercase or lowercase; other characters are the same
# spam = 'Hello, world'
# spam = spam.upper()
# print(spam)
# spam = spam.lower()
# print(spam)
# methods don't change the string itself but returns new string values; if you want to you have to assign to a var


# these methods help for case sensitive things
# print('How are you?')
# feeling = input()
# if feeling.lower() == 'great':
#     print('I feel great too.')
# else:
#     print('I hope the rest of your day is good')


# isupper() ; islower()
# returns True if the string has at least 1 letter and all of them are lower or upper, otherwise it returns False
# spam = 'Hello, world!'
# print(spam.islower())
# print(spam.isupper())
# print('HELLO'.isupper())
# print('abc12345'.islower())
# print('12345'.islower())
# print('12345'.isupper())

print('Hello'.upper())
print('Hello'.upper().lower()) # 'Hello' to uppercase: HELLO, then lowercase it: 'hello'
print('Hello'.upper().lower().upper())
print('HELLO'.lower())
print('HELLO'.lower().islower()) # convert HELLO to lowercase so hello, then see whether it is lowercase(True) or not(False)