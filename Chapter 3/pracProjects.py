def collatz(number):
    if (number %2 == 0):
        print (number // 2)
        return int(number // 2)
    elif (number %2 == 1):
        print (3 * number + 1)
        return int(3 * number + 1)

user_in = int(input())  # everything on the right goes inside the 'bucket'
new_var = collatz(user_in) # new bucket
while True:
    if (new_var == 1):
        break
    else:
        new_var = collatz(new_var) # new bucket value replaces old
        print(new_var) # keeps looping until the value breaks at 1

print("good job!")

def collatz(number):
    if (number %2 == 0):
        print (number // 2)
        return int(number // 2)
    elif (number %2 == 1):
        print (3 * number + 1)
        return int(3 * number + 1)

try:
    user_in = int(input())  # everything on the right goes inside the 'bucket'
    new_var = collatz(user_in)
    while True:
        if (new_var == 1):
            break
        else:
            new_var = collatz(new_var)
            print(new_var)

except ValueError:
    print('Please enter and integer.')
