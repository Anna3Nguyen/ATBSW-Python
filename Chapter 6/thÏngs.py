# review: string concatenation
# name = 'Al'
# age = 4000
# print('Hello, my name is ' + name + '. I am ' + str(age) + ' years old.')

# string interpolation:
# name = 'Al'
# age = 4000
# print('My name is %s. I am %s years old.' %(name, age)) # use % operators inside string to act as a marker
# then replace the % with variables that represent the values going inside of the % in a key outside of the string in ()

# f strings (use braces instead of %, use the f prefix beforehand)
# name = 'Al'
# age = 4000
# print(f'My name is {name}. Next year I will be {age + 1}.') # FOR PYTHON 3.6 (f doesn't work here)
# My name is Al. Next year I will be 4001.
# remember to include f, otherwise the braces and stuff will be strings
# print('My name is {name}. Next year I will be {age + 1}.')
# My name is {name}. Next year I will be {age + 1}.
