# 1. What is []?
# it represents an empty list
# 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam?
# (Assume spam contains [2, 4, 6, 8, 10].)
# spam.insert(2, 'hello') or spam[2] = 'hello'
#  For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
#
# 3. What does spam[int(int('3' * 2) // 11)] evaluate to?
#  'd'
# 4. What does spam[-1] evaluate to?
# 'd'
# 5. What does spam[:2] evaluate to?
# ['a','b')
# For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].
#
# 6. What does bacon.index('cat') evaluate to?
# 1
# 7. What does bacon.append(99) make the list value in bacon look like?
# [3.14, 'cat', 11, 'cat', True, 99]
# 8. What does bacon.remove('cat') make the list value in bacon look like?
# [3.14, 11, 'cat', True]
# 9. What are the operators for list concatenation and list replication?
# list contenation: + replication: *
# 10. What is the difference between the append() and insert() list methods?
# append adds the value at the end of the list while insert puts values in at a certain index
# 11. What are two ways to remove values from a list?
# del() or remove()
# 12. Name a few ways that list values are similar to string values.
# both are enclosed by some sort of brackets/parentheses, can replicate and contacentate same way, put in ''
# can be passed to len(), have indexes and slices, can be used in loops, used with the in and not operators
# 13. What is the difference between lists and tuples?
# Tuples are immutable while lists are mutable and tuples have ()
# 14. How do you type the tuple value that has just the integer value 42 in it?
# (42,)
# 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
# Use the tuple() function to find tuple of a list and list() of the tuple to find the list form
# 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
# They contain references to lists
# 17. What is the difference between copy.copy() and copy.deepcopy()?
# copy.copy() duplicates a copy of a mutable value, not just a reference copy. copy.deepcopy() copies inner lists