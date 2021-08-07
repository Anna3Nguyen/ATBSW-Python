# pprint() makes the code look better and has a cleaner display of the dictionary than print()
# is very helpful when the dictionary has nested lists or dictionaries
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count) # = print(pprint.pformat(count)
# pprint.pformat() will turn the pretty text to a string value instead of showing it on screen
