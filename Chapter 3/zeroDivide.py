# def spam(divideBy):
#     return 42/divideBy
#
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))



# def spam(divideBy):
#     try:
#         return 42/divideBy
#     except ZeroDivisionError:
#         print('Error: Invalid argument.')
#
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# The code that could potentially have an error is put in a try clause.
# The program execution moves to the start of a following except clause if an error happens.


def spam(divideBy):
    return 42/divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
