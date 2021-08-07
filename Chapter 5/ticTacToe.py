theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ' }
def printBoard(board):#parameter board doesn't have much meaning but it's helpful if you want to use it with several diff parameters
    # its pretty much like a variable that's there but gets replaced when you define your new parameters to use
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard) # parameter (theBoard); the function is called so you go to line 4 to see its data to print it
# and when you do, you will replace the function parameter that is currently board, with theBoard,
# so everytime you now see board in the function printBoard, it will be replaced with theBoard
