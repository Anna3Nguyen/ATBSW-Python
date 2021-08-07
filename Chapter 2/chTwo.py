# Boolean data has two values: True or False
# spam = True
# print (spam)
# print (true)
# True = 2+2
# If you don't use proper case or use True or False for a variable name, Python gives error message
# comparison_Operators or relational operators:
# == equal to
# != not equal to
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to
# print (42 == 42)
# print (42==99)
# print (2 != 3)
# print (2 != 2)
# print ('hello' =='hello')
# print ('hello'=='Hello')
# print ('dog'!= 'cat')
# print (True == True)
# print (True != False)
# print (42==42.0)
# print (42=='42')
# print (42<100)
# print (42>100)
# print (42<42)
# eggCount=42
# print (eggCount <= 42)
# myAge=29
# print (myAge >= 10)
# == (equal to) asks whether two values are the same
# = (assignment) puts the value on the right into the variable on the left
#Boolean Operators (and, or, and not)
# and & or take two Boolean values or expressions so they're binary operators
#The and operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False.
# print (True and True)
# print (True and False)
# Truth Table for and
# True and True evaluates to True
# True and False eval. to False
# False and True eval. to False
# False and False eval. to False
#the or operator evaluates an expression to True if either of the two Boolean values is True. If both are False,
# it evaluates to False.
# print (False or True)
# print (False or False)
# Unlike and and or, the not operator operates on only one Boolean value (or expression).
# This makes it a unary operator. The not operator simply evaluates to the opposite Boolean value.
# print (not True)
# print (not not not not True)
# not operator Truth Table
# not True eval. to False
# not False eval. to True
# print (4<5) and (5<6)
# print ((4<5) and (9<6))
# print ((1==2) or (2==2))
# print (2+2==4 and not 2+2==5 and 2*2==2+2)
# After any math and comparison operators evaluate,
# Python evaluates the not operators first, then the and operators, and then the or operators.