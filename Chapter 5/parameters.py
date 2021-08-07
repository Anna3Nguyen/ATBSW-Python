num3 = 2
num4 = 3
def add(num1, num2): # replace the parameters num1 with num3 and num2 with num4
    total = num1 + num2
    return total
print(add(num3, num4)) # more convenient to have variables in the instance that you have to keep calling code many times
# so instead of having to change the parameters assigned (numbers) again and again, you can just change the variables once
# and it will work the same!