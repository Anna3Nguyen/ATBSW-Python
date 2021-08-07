# rjust() and ljust()
# print('Hello'.rjust(10)) # right justify 'Hello' in a total string length of 10
# print('Hello'.rjust(20)) # 20 character spaces including the string 'Hello' # string is to the very right
# print('Hello, World'.rjust(20))
# print('Hello'.ljust(10)) # string is to the very left

# 2nd argument to insert a character other than a space:
# print('Hello'.rjust(20, '*'))
# print('Hello'.ljust(20, '-'))

# center() ; centers text
# print('Hello'.center(20))
# print('Hello'.center(20, '='))


# removing whitespace with strip() ; rstrip() ; lstrip()
# strip() returns a string without any whitespace characters at the start or end
# lstrip() and rstrip() remove space characters from the left or right ends
# spam = '   Hello, World   '
# print(spam.strip())
# print(spam.lstrip())
# print(spam.rstrip())

# optional argument added to specify which characters on which ends should be stripped
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS')) # tells it to strip occurrences of a, m, p, and S from the ends of spam
# order of the charcters does not matter