# Mutable data like lists will reference the one list that they equal to so for ex.
# x = [1, 2, 3] y = x x.append('lol') print(x) = [1,2,3, 'lol'] which y also equals as well
# Immutable data doesnt do that for ex.
# x = 'hello' y = x; x = x + 'there' print(x) = 'hello there' while y is 'hello' still
grid = [['.','.','.','.','.','.'],
 ['.','O','O','.','.','.'],
 ['O','O','O','O','.',','],
 ['O','O','O','O','O','.'],
 ['.','O','O','O','O','O'],
 ['O','O','O','O','O','.'],
 ['O','O','O','O','.','.'],
 ['.','O','O','.','.','.'],
 ['.','.','.','.','.','.']]
