# Parameters and variables that are assigned in a called function are said to exist in that function’s local scope.
# Variables that are assigned outside all functions are said to exist in the global scope.
# A variable must be one or the other; it cannot be both local and global.
# There is only one global scope, and it is created when your program begins. When program terminates all is gone.
# A local scope is created whenever a function is called. When it returns, variables are forgotten.

# Code in the global scope, outside of all functions, cannot use any local variables.
# However, code in a local scope can access global variables.
# Code in a function’s local scope cannot use variables in any other local scope.
# You can use the same name for different variables if they are in different scopes.

# error program:
# def spam():
#     eggs = 31337
# spam()
# print(eggs)

# The local scope eggs is forgotten after the function spam returns and also global scope can't access local scope


# Local Scopes cannot use variables in other local scopes:

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
