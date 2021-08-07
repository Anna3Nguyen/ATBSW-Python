# def commaCode():
#     spam = ['apples','bananas','tofu','cats']
#     print('Enter an item.')
#     newSpam = input()
#     print(newSpam)
#
#     if newSpam in spam:
#         print('apples, bananas, tofu, and cats')
#
#     else:
#         print('sorry, not the right input, please try again')
#         commaCode()
#
# commaCode()

spam = ['apples','bananas', 'tofu','cats']
someParameter = input()
def commaCode(someParameter):
    while True:
        if someParameter == spam:
            print(str(spam[:2]+'and'+str(spam[-1])))
            break
        else:
            print('Try again. Enter a new list value or var that list is stored in.')


