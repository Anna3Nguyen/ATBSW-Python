# isX() Methods return True or False depending on the contents of the string

''' isapha() returns True if the string consists of letters ONLY and isn't blank ; is alphabet
isalnum() returns True if the string consists only of letters and #s and is not blank ; is alphabet and numbers
isdecimal() returns True fi the string consists of only numeric characters and not blank ; is decimal == numeric
isspace() returns True if not blank and consists of only spaces, tabs, and newlines ; is spaces and other things with space
istitle() returns True if string has only of words that start with an uppercase letter followed by only lowercase ; like titles'''

# print('hello'.isalpha())
# print('hello123'.isalpha())
# print('hello123'.isalnum())
# print('hello'.isalnum()) # letters or numbers too, doesn't have to be both
# print('123'.isdecimal())
# print('     '.isspace())
# print('This Is Title Case'.istitle())
# print('This Is Title Case 123'.istitle()) # can include numbers
# print('This Is not Title Case'.istitle())
# print('This Is NOT Title Case Either'.istitle())



# startswith() ; endswith() Methods:
# returns True or False depending on if the string value they called on starts of ends with the string passed to the method
print('Hello, world!'.startswith('Hello'))
print('Hello, world!'.endswith('world!'))
print('abc123'.startswith('abcdef'))
print('abc123'.endswith('12')) # False; close to the end but is not the actual end
print('Hello, world!'.startswith('Hello, world!')) # True
print('Hello, world!'.endswith('Hello, world!')) # True
# this methods are alternatives to the == operator if you need to see if the first or last part instead of the whole thing
# is equal to another string