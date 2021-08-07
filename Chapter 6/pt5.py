# Computers store information as bytes—strings of binary numbers, which means we need to be able to convert text
# to numbers. Because of this, every text character has a corresponding numeric value called a Unicode code point.

print(ord('A')) # ord() gets the code point of a 1 character string
print(ord('4'))
print(ord('!'))
print(chr(65)) # chr() gets the one character string of an integer code point

print(ord('B'))
print(ord('A')< ord('B'))
print(chr(ord('A')))
print(chr(ord('A')+1))