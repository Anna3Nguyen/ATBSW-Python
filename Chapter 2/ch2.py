# Flow control statements often start with a part called the condition
# and are always followed by a block of code called the clause.
# Conditions always evaluate down to a Boolean value; a flow control statement decides what to do based on condition
# Blocks begin when the indentation increases.
# Blocks can contain other blocks.
# Blocks end when the indentation decreases to zero or to a containing block’s indentation.
name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print ('Hello, Mary')
    if password == 'swordfish':
        print ('Access granted')
    else:
        print ('Wrong password')

#if is the most common flow control statement
# In plain English, an if statement could be read as, “If this condition is true, execute the code in the clause.
# ” In Python, an if statement consists of the following:
# The if keyword
# A condition (that is, an expression that evaluates to True or False)
# A colon
# Starting on the next line, an indented block of code (called the if clause)
# “If this condition is true, execute this code. Or else, execute that code.”
# An else statement doesn’t have a condition, and in code, an else statement always consists of the following:
# The else keyword
# A colon
# Starting on the next line, an indented block of code (called the else clause)
# The elif statement is an “else if” statement that always follows an if or another elif statement.
# It provides another condition that is checked only if all of the previous conditions were False.
# In code, an elif statement always consists of the following:
# The elif keyword
# A condition (that is, an expression that evaluates to True or False)
# A colon
# Starting on the next line, an indented block of code (called the elif clause)