import random
numberOfStreaks = 0
inARow = 0
coinFlip = []
heads = 'H'
tails = 'T'

for experimentNumber in range(10000):
    for flips in range(100):
        if random.randint(0,1) == 0:
            result = heads
        elif random.randint(0,1) == 1:
            result = tails
        output = result
        print(output)

        coinFlip.append(output)
        if (flips-1) < 0:
            pass
        elif coinFlip[flips-1] == output:
            inARow += 1
            if inARow == 6:
                numberOfStreaks += 1
            else:
                inARow += 0

        coinFlip = []
print('chance of streak: %s%%' % (numberOfStreaks / 100))


