# keys() values() and items() methods will return list like values but not true lists; don't have append() or be modified
# they can be used in for loops though

# spam = {'color': 'red', 'age': 42}
# for v in spam.values():
#     print(v)

# for k in spam.keys():
#     print(k)

# for i in spam.items():
#     print(i)

# dict_keys, dict_values, and dict_items
# data types which are dictionary data types, not true lists

spam = {'color': 'red', 'age': 42}
print(spam.keys())
print(list(spam.keys()))

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))


