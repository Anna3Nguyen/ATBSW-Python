# import random
# numberOfStreaks = 0
# H = 'heads'
# T = 'tails'
#
# for experimentNumber in range(10000): # Code that creates a list of 100 'heads' or 'tails' values
#     if random.randint(0, 1) == 0:
#         print(list('H'))
#     elif random.randint(0, 1) == 1:
#         print(list('T'))
#
# if H or T == 6:
#     numberOfStreaks += 1
#     currentStreaks = numberOfStreaks
#     print('Chance of streak: %s%%' % (currentStreaks / 100))Code that checks if there is a streak of 6 heads or tails in a row


# Make a variable for the flips # in one experiment with a double for loop
    # append the coin flip value to the coin flip list for experiment 1
    # coin flip - 1 to check the index of previous coin flip to see if it is matching to form it in a row times
    # if it doesn't match then the streak ends
    # if it reaches 6 then add to the number of streaks
    # then repeat for experiment 2 and reset

import random
numberOfStreaks = 0
inARow = 0
heads = 'H'
tails = 'T'
coinFlip = []

for experimentNumber in range(10000): # Code that creates a list of 100 'heads' or 'tails' values
    for flips in range(100): # Double for loops (make 100 flips)
        if random.randint(0,1) == 0:
            output = heads
        elif random.randint(0,1) == 1:
            output = tails
        result = output
        print(list(result))

        coinFlip.append(result) # Adds H or T after whatever is in the list coinFlip
        if (flips-1) < 0:
            pass
        elif coinFlip[flips-1] == result:
            inARow += 1
            if inARow == 6:
                numberOfStreaks += 1
            else:
                numberOfStreaks += 0
    coinFlip = []

print('Chance of streak: %s%%' % (numberOfStreaks / 100)) # Code that checks if there is a streak of 6 heads or tails in a row



