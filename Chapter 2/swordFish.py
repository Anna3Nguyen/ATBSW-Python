while True:
    print ('Who are you?')
    name = input()
    if name != ('Joe'):
        continue
    print ('Hello, Joe. What is the password?(It is a fish.)')
    password = input()
    if password == ('swordfish'):
        break
print ('Access granted.')

# When used in conditions, 0, 0.0, and '' (the empty string) are considered False,
# while all other values are considered True.


