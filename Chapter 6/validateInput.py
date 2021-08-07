while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal(): # if the age input is numeric then break out of the loop
        break
    print('Please enter a number for your age.') # otherwise it will keep looping until it gets a good output

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passwords can only have letters and numbers.')