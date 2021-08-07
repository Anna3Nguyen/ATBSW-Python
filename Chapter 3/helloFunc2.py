# When you call the print() or len() function, you pass them values, called arguments, by typing them between the parentheses.

def hello(name):
    print('Hello,' + name)

hello('Alice')
hello('Bob')

# Parameters are variables that contain arguments.

def sayHello(name):
    print('Hello'+ name)
sayHello('Al')

# To define a function is to create it, just like an assignment statement like spam = 42 creates the spam variable.
# The argument 'Al' is assigned to a local variable named name. Variables that have arguments assigned to them are parameters.

# the value that a function call evaluates to is called the return value of the function.
# When creating a function using the def statement, you can specify what the return value should be with a return statement.
#  A return statement consists of the following:
# The return keyword
# The value or expression that the function should return