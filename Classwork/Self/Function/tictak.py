from random import randint as ra



theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys =[]

# for key in theBoard:
#  board_keys.append(key)


def printBoard(board):
    print(board['7'] + '  |' + board['8'] + '  |' + board['9']+'  |7| |8| |9|')
    print('---|---|---')
    print(board['4'] + '  |' + board['5'] + '  |' + board['6']+'  |4| |5| |6|')

    print('---|---|---')
    print(board['1'] + '  |' + board['2'] + '  |' + board['3']+'  |1| |2| |3|')


def gameplay():

    printBoard(theBoard)
    S_Turn = ra(1,2)

    if S_Turn==0:
        print("X's turn")
        turn ="X"
    else:
        print("O's turn")
        turn ="O"
        count=0

    for i in range(10):

        print(f"it's your turn:{turn}")
        move=input("Enter input:")

        if theBoard[move]== ' ' :
            theBoard[move]=turn
            printBoard(theBoard)
            count+=1
        else:
            print("Jagya nathi bhai")
            continue
        
        if count>=5:

            if theBoard['7']==theBoard['8']==theBoard['9']!= ' ' :
                print(f"{turn} win the game")
                break
            elif theBoard['4']==theBoard['5']==theBoard['6']!= ' ' :
                 print(f"{turn} win the game")
                 break
            elif theBoard['1']==theBoard['2']==theBoard['3']!= ' ' :
                 print(f"{turn} win the game")
                 break
             #column
            elif theBoard['7']==theBoard['4']==theBoard['1']!= ' ' :
                 print(f"{turn} win the game")
                 break
            elif theBoard['8']==theBoard['5']==theBoard['2']!= ' ' :
                 print(f"{turn} win the game")
                 break
            elif theBoard['9']==theBoard['6']==theBoard['3']!= ' ' :
                 print(f"{turn} win the game")
                 break
             #cross
            elif theBoard['7']==theBoard['5']==theBoard['3']!=  ' ' :
                 print(f"{turn} win the game")
                 break
            elif theBoard['9']==theBoard['5']==theBoard['1']!= ' ' :
                 print(f"{turn} win the game")
                 break
            #tie the board
            if count==9:
                print("Game Over")
                break

        if turn=='X':
            turn = 'O'
        else:
            turn='X'
                
        
gameplay()