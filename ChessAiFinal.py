def genboard():
    woff = 10
    boff = 20
    pawn = 0
    knight = 1
    bishop = 2
    rook = 3
    queen = 4
    king = 5
    board = []
    for i in range(0,64):
        board = board + [0]
    board[0] = 10 + 3
    board[1] = 10 + 1
    board[2] = 10 + 2
    board[3] = 10 + 4
    board[4] = 10 + 5
    board[5] = 10 + 2
    board[6] = 10 + 1
    board[7] = 10 + 3
    for i in range(0,8,1):
        board[8+i] = 10
    board[56] = 20 + 3
    board[57] = 20 + 1
    board[58] = 20 + 2
    board[59] = 20 + 4
    board[60] = 20 + 5
    board[61] = 20 + 2
    board[62] = 20 + 1
    board[63] = 20 + 3
    for i in range(0, 8, 1):
        board[48 + i] = 20
    return board
board = genboard()

def printlist(board):
    white = ["P","H","B","R","Q","K"]
    black = ["p","h","b","r","q","k"]
    print(board)
    h = 0
    for i in range(8,0,-1):
        for j in range(8,0,-1):
            a = 8*i - j
            if board[a] == 0 and a>9:
                print(str(a), end=" ")
            if board[a] == 0 and a<10:
                print(str(a)+" ", end=" ")
            if board[a] == 10:
                print("WP", end=" ")
            if board[a] == 11:
                print("WH", end=" ")
            if board[a] == 12:
                print("WB", end=" ")
            if board[a] == 13:
                print("WR", end=" ")
            if board[a] == 14:
                print("WQ", end=" ")
            if board[a] == 15:
                print("WK", end=" ")
            if board[a] == 20:
                print("bp", end=" ")
            if board[a] == 21:
                print("bh", end=" ")
            if board[a] == 22:
                print("bb", end=" ")
            if board[a] == 23:
                print("br", end=" ")
            if board[a] == 24:
                print("bq", end=" ")
            if board[a] == 25:
                print("bk", end=" ")
            if j == 1:
                print("")
    return True

def printboard(board):
    white = ["P","H","B","R","Q","K"]
    black = ["p","h","b","r","q","k"]
    print(board)
    h = 0
    for i in range(8,0,-1):
        for j in range(8,0,-1):
            a = 8*i - j
            if board[a] == 0:
                if (a+h)%2 == 0:
                    print("##", end=" ")
                else:
                    print("__", end=" ")
            if board[a] == 10:
                print("WP", end=" ")
            if board[a] == 11:
                print("WH", end=" ")
            if board[a] == 12:
                print("WB", end=" ")
            if board[a] == 13:
                print("WR", end=" ")
            if board[a] == 14:
                print("WQ", end=" ")
            if board[a] == 15:
                print("WK", end=" ")
            if board[a] == 20:
                print("bp", end=" ")
            if board[a] == 21:
                print("bh", end=" ")
            if board[a] == 22:
                print("bb", end=" ")
            if board[a] == 23:
                print("br", end=" ")
            if board[a] == 24:
                print("bq", end=" ")
            if board[a] == 25:
                print("bk", end=" ")
            if j == 1:
                print("")
                if h == 0:
                    h =1
                elif h == 1:
                    h = 0
    return True

def GetPlayerPositions(board,player):
    pos = []
    if player == 10:
        for i in range(0,64,1):
            if (board[i] >9) and (board[i]<19):
                pos = pos + [i]
        print("white occupies")
        print(pos)
        return pos
    elif player == 20:
        for i in range(0,64,1):
            if (board[i] >19) and (board[i]<29):
                pos = pos + [i]
        print("black occupies")        
        print(pos)
        return pos

def GetPieceLegalMoves(board,position):
    legalmoves = []
    if board[position] == 10: #whitepawn
        if position+8>63:
            return legalmoves
        if board[position + 8] == 0:
            legalmoves = legalmoves + [position +8]
        if (board[position +7] > 19) and ((position%8) != 0):
            legalmoves = legalmoves + [position +7]
        if (board[position +9] > 19) and ((position%8) != 7):
            legalmoves = legalmoves + [position +9]
    if board[position] == 13: # whiterook
        for i in range(1,8,1): # foward
            if position + 8*i > 63:
                break
            elif board[position + 8*i] == 0:
                legalmoves = legalmoves + [position + 8*i]
            elif board[position + 8*i] > 19:
                legalmoves = legalmoves + [position + 8*i]
                break
            else:
                break
        for i in range(1, 8, 1):  # backward
            if position - 8*i < 0:
                break
            elif board[position - 8 * i] == 0:
                legalmoves = legalmoves + [position - 8 * i]
            elif board[position - 8 * i] > 19:
                legalmoves = legalmoves + [position - 8 * i]
                break
            else:
                break
        for i in range(1,8,1): # right
            if (position + i)%8 == 0:
                break
            elif board[position +i] >19:
                legalmoves = legalmoves + [position+i]
                break
            elif board[position+i] == 0:
                legalmoves = legalmoves + [position+i]
            else:
                break
        for i in range(1, 8, 1):  # left
            if position == 0:
                break
            if (position - i) % 8 == 7:
                break
            elif board[position - i] > 19:
                legalmoves = legalmoves + [position - i]
                break
            elif board[position - i] == 0:
                legalmoves = legalmoves + [position - i]
            else:
                break
    if board[position] == 12: # white bishop
        for i in range(1,8,1): #forward left
            if position + 7*i > 63:
                break
            if (position+7*i)%8 == 7:
                break
            elif(board[position +7*i]) == 0:
                legalmoves = legalmoves + [position +7*i]
            elif (board[position +7*i]) > 19:
                legalmoves = legalmoves + [position + 7*i]
                break
            else:
                break
        for i in range(1,8,1): #forward right
            if position + 9*i > 63:
                break
            if (position+9*i)%8 == 0:
                break
            elif(board[position +9*i]) == 0:
                legalmoves = legalmoves + [position +9*i]
            elif (board[position +9*i]) > 19:
                legalmoves = legalmoves + [position + 9*i]
                break
            else:
                break
        for i in range(1,8,1): #back left
            if position - 9*i <0:
                break
            if (position-9*i)%8 == 7:
                break
            elif(board[position -9*i]) == 0:
                legalmoves = legalmoves + [position -9*i]
            elif (board[position -9*i]) > 19:
                legalmoves = legalmoves + [position - 9*i]
                break
            else:
                break
        for i in range(1,8,1): #back right
            if position - 7*i <0:
                break
            if (position-7*i)%8 == 0:
                break
            elif(board[position -7*i]) == 0:
                legalmoves = legalmoves + [position -7*i]
            elif (board[position -7*i]) > 19:
                legalmoves = legalmoves + [position - 7*i]
                break
            else:
                break
    if board[position] == 11: #whiteknight
        if (position + 15) < 64:
            if ((board[position + 15] > 19) or (board[position + 15] == 0)) and (position%8 != 0): #bigforwardleft
                legalmoves = legalmoves + [position + 15]
        if (position + 17) < 64:
            if ((board[position + 17] > 19) or (board[position + 17] == 0)) and (position%8 != 7): #bigforwardright
                legalmoves = legalmoves + [position + 17]
        if (position + 10) < 64:
            if ((board[position + 10] > 19) or (board[position + 10] == 0) and (position%8 != 7)) and (position%8 !=6): #smallforwardright
                legalmoves = legalmoves + [position + 10]
        if (position + 6) < 64:
            if ((board[position + 6] > 19) or (board[position + 6] == 0)) and (position%8 != 1) and (position%8 !=0): #smallforwardleft
                legalmoves = legalmoves + [position + 6]
        if (position - 10) > 0:
            if ((board[position -10] > 19) or (board[position -10] == 0)) and (position%8 != 0) and (position%8 !=1): #smallbackwardleft
                legalmoves = legalmoves + [position -10]
        if (position - 6) > 0:
            if ((board[position -6] > 19) or (board[position -6] == 0)) and (position%8 != 7) and (position%8 !=6): #smallbackwardright
                legalmoves = legalmoves + [position -6]
        if (position - 15) > 0:
            if ((board[position - 15] > 19) or (board[position - 15] == 0)) and (position%8 != 7): #bigbackwardright
                legalmoves = legalmoves + [position - 15]
        if (position - 17) > 0:
            if ((board[position - 17] > 19) or (board[position -17] == 0)) and (position%8 !=0): #bigbackwardleft
                legalmoves = legalmoves + [position - 17]
    if board[position] == 14: # whitequeen
        for i in range(1,8,1): # foward
            if position + 8*i > 63:
                break
            elif board[position + 8*i] == 0:
                legalmoves = legalmoves + [position + 8*i]
            elif board[position + 8*i] > 19:
                legalmoves = legalmoves + [position + 8*i]
                break
            else:
                break
        for i in range(1, 8, 1):  # backward
            if position - 8*i < 0:
                break
            elif board[position - 8 * i] == 0:
                legalmoves = legalmoves + [position - 8 * i]
            elif board[position - 8 * i] > 19:
                legalmoves = legalmoves + [position - 8 * i]
                break
            else:
                break
        for i in range(1,8,1): # right
            if (position + i)%8 == 0:
                break
            elif board[position +i] >19:
                legalmoves = legalmoves + [position+i]
                break
            elif board[position+i] == 0:
                legalmoves = legalmoves + [position+i]
            else:
                break
        for i in range(1, 8, 1):  # left
            if position == 0:
                break
            if (position - i) % 8 == 7:
                break
            elif board[position - i] > 19:
                legalmoves = legalmoves + [position - i]
                break
            elif board[position - i] == 0:
                legalmoves = legalmoves + [position - i]
            else:
                break
        for i in range(1,8,1): #forward left
            if position + 7*i > 63:
                break
            if (position+7*i)%8 == 7:
                break
            elif(board[position +7*i]) == 0:
                legalmoves = legalmoves + [position +7*i]
            elif (board[position +7*i]) > 19:
                legalmoves = legalmoves + [position + 7*i]
                break
            else:
                break
        for i in range(1,8,1): #forward right
            if position + 9*i > 63:
                break
            if (position+9*i)%8 == 0:
                break
            elif(board[position +9*i]) == 0:
                legalmoves = legalmoves + [position +9*i]
            elif (board[position +9*i]) > 19:
                legalmoves = legalmoves + [position + 9*i]
                break
            else:
                break
        for i in range(1,8,1): #back left
            if position - 9*i <0:
                break
            if (position-9*i)%8 == 7:
                break
            elif(board[position -9*i]) == 0:
                legalmoves = legalmoves + [position -9*i]
            elif (board[position -9*i]) > 19:
                legalmoves = legalmoves + [position - 9*i]
                break
            else:
                break
        for i in range(1,8,1): #back right
            if position - 7*i <0:
                break
            if (position-7*i)%8 == 0:
                break
            elif(board[position -7*i]) == 0:
                legalmoves = legalmoves + [position -7*i]
            elif (board[position -7*i]) > 19:
                legalmoves = legalmoves + [position - 7*i]
                break
            else:
                break
    if board[position] == 15: # whiteking
        for i in range(1,2,1): # foward
            if position + 8*i > 63:
                break
            elif board[position + 8*i] == 0:
                legalmoves = legalmoves + [position + 8*i]
            elif board[position + 8*i] > 19:
                legalmoves = legalmoves + [position + 8*i]
                break
            else:
                break
        for i in range(1, 2, 1):  # backward
            if position - 8*i < 0:
                break
            elif board[position - 8 * i] == 0:
                legalmoves = legalmoves + [position - 8 * i]
            elif board[position - 8 * i] > 19:
                legalmoves = legalmoves + [position - 8 * i]
                break
            else:
                break
        for i in range(1,2,1): # right
            if (position + i)%8 == 0:
                break
            elif board[position +i] >19:
                legalmoves = legalmoves + [position+i]
                break
            elif board[position+i] == 0:
                legalmoves = legalmoves + [position+i]
            else:
                break
        for i in range(1, 2, 1):  # left
            if position == 0:
                break
            if (position - i) % 8 == 7:
                break
            elif board[position - i] > 19:
                legalmoves = legalmoves + [position - i]
                break
            elif board[position - i] == 0:
                legalmoves = legalmoves + [position - i]
            else:
                break
        for i in range(1,2,1): #forward left
            if position + 7*i > 63:
                break
            if (position+7*i)%8 == 7:
                break
            elif(board[position +7*i]) == 0:
                legalmoves = legalmoves + [position +7*i]
            elif (board[position +7*i]) > 19:
                legalmoves = legalmoves + [position + 7*i]
                break
            else:
                break
        for i in range(1,2,1): #forward right
            if position + 9*i > 63:
                break
            if (position+9*i)%8 == 0:
                break
            elif(board[position +9*i]) == 0:
                legalmoves = legalmoves + [position +9*i]
            elif (board[position +9*i]) > 19:
                legalmoves = legalmoves + [position + 9*i]
                break
            else:
                break
        for i in range(1,2,1): #back left
            if position - 9*i <0:
                break
            if (position-9*i)%8 == 7:
                break
            elif(board[position -9*i]) == 0:
                legalmoves = legalmoves + [position -9*i]
            elif (board[position -9*i]) > 19:
                legalmoves = legalmoves + [position - 9*i]
                break
            else:
                break
        for i in range(1,2,1): #back right
            if position - 7*i <0:
                break
            if (position-7*i)%8 == 0:
                break
            elif(board[position -7*i]) == 0:
                legalmoves = legalmoves + [position -7*i]
            elif (board[position -7*i]) > 19:
                legalmoves = legalmoves + [position - 7*i]
                break
            else:
                break



    if board[position] == 20: #blackpawn
        if position-8<0:
            return legalmoves
        if board[position - 8] == 0:
            legalmoves = legalmoves + [position -8]
        if (board[position -7] > 9) and (board[position -7] < 19) and ((position%8) != 7):
            legalmoves = legalmoves + [position -7]
        if (board[position -9] < 19) and (board[position -9] > 9) and ((position%8) != 0):
            legalmoves = legalmoves + [position -9]
    if board[position] == 23: # blackrook
        for i in range(1,8,1): # backward
            if position + 8*i > 63:
                break
            elif board[position + 8*i] == 0:
                legalmoves = legalmoves + [position + 8*i]
            elif (board[position + 8*i] < 19) and (board[position + 8*i] > 9):
                legalmoves = legalmoves + [position + 8*i]
                break
            else:
                break
        for i in range(1, 8, 1):  # forward
            if position - 8*i < 0:
                break
            elif board[position - 8 * i] == 0:
                legalmoves = legalmoves + [position - 8 * i]
            elif (board[position - 8 * i] < 19) and (board[position - 8 * i] > 9):
                legalmoves = legalmoves + [position - 8 * i]
                break
            else:
                break
        for i in range(1,8,1): # right
            if (position + i)%8 == 0:
                break
            elif (board[position +i] <19) and (board[position + i] >9):
                legalmoves = legalmoves + [position+i]
                break
            elif board[position+i] == 0:
                legalmoves = legalmoves + [position+i]
            else:
                break
        for i in range(1, 8, 1):  # left
            if position == 0:
                break
            if (position - i) % 8 == 7:
                break
            elif (board[position - i] < 19) and (board[position - i] > 9):
                legalmoves = legalmoves + [position - i]
                break
            elif board[position - i] == 0:
                legalmoves = legalmoves + [position - i]
            else:
                break
    if board[position] == 22: # black bishop
        for i in range(1,8,1): #backward left
            if position + 7*i > 63:
                break
            if (position+7*i)%8 == 7:
                break
            elif(board[position +7*i]) == 0:
                legalmoves = legalmoves + [position +7*i]
            elif ((board[position +7*i]) < 19) and ((board[position +7*i]) > 9):
                legalmoves = legalmoves + [position + 7*i]
                break
            else:
                break
        for i in range(1,8,1): #backward right
            if position + 9*i > 63:
                break
            if (position+9*i)%8 == 0:
                break
            elif(board[position +9*i]) == 0:
                legalmoves = legalmoves + [position +9*i]
            elif (board[position +9*i]) < 19 and (board[position +9*i]) > 19:
                legalmoves = legalmoves + [position + 9*i]
                break
            else:
                break
        for i in range(1,8,1): #forward left
            if position - 9*i <0:
                break
            if (position-9*i)%8 == 7:
                break
            elif(board[position -9*i]) == 0:
                legalmoves = legalmoves + [position -9*i]
            elif (board[position -9*i]) < 19:
                legalmoves = legalmoves + [position - 9*i]
                break
            else:
                break
        for i in range(1,8,1): #forward right
            if position - 7*i <0:
                break
            if (position-7*i)%8 == 0:
                break
            elif(board[position -7*i]) == 0:
                legalmoves = legalmoves + [position -7*i]
            elif (board[position -7*i]) < 19 and (board[position -7*i]) > 9:
                legalmoves = legalmoves + [position - 7*i]
                break
            else:
                break
    if board[position] == 21: #blackknight
        if (position + 15) < 64:
            if ((board[position + 15] < 19) or (board[position + 15] == 0)) and (position%8 != 0): #bigbackwardleft
                legalmoves = legalmoves + [position + 15]
        if (position + 17) < 64:
            if ((board[position + 17] < 19) or (board[position + 17] == 0)) and (position%8 != 7): #bigbackwardright
                legalmoves = legalmoves + [position + 17]
        if (position + 10) < 64:
            if (board[position + 10] < 19) or (board[position + 10] == 0) and (position%8 != 7) and (position%8 !=6): #smallbackwardright
                legalmoves = legalmoves + [position + 10]
        if (position + 6) < 64:
            if ((board[position + 6] < 19) or (board[position + 6] == 0)) and (position%8 != 1) and (position%8 !=0): #smallbackwardleft
                legalmoves = legalmoves + [position + 6]
        if (position - 10) > 0:
            if ((board[position -10] < 19) or (board[position -10] == 0)) and (position % 8 != 0) and (position % 8 != 1): #smallforwardleft
                legalmoves = legalmoves + [position -10]
        if (position - 6) > 0:
            if ((board[position -6] < 19) or (board[position -6] == 0)) and (position%8 != 7) and (position%8 !=6): #smallforwardright
                legalmoves = legalmoves + [position -6]
        if (position - 15) > 0:
            if ((board[position - 15] < 19) or (board[position - 15] == 0)) and (position%8 != 7): #bigforwardright
                legalmoves = legalmoves + [position - 15]
        if (position - 17) > 0:
            if ((board[position - 17] < 19) or (board[position -17] == 0)) and (position%8 !=0): #bigforwardleft
                legalmoves = legalmoves + [position - 17]
    if board[position] == 24: # blackqueen
        for i in range(1,8,1): # backward
            if position + 8*i > 63:
                break
            elif board[position + 8*i] == 0:
                legalmoves = legalmoves + [position + 8*i]
            elif (board[position + 8*i] < 19) and (board[position + 8*i] > 9):
                legalmoves = legalmoves + [position + 8*i]
                break
            else:
                break
        for i in range(1, 8, 1):  # forward
            if position - 8*i < 0:
                break
            elif board[position - 8 * i] == 0:
                legalmoves = legalmoves + [position - 8 * i]
            elif (board[position - 8 * i] < 19) and (board[position - 8 * i] > 9):
                legalmoves = legalmoves + [position - 8 * i]
                break
            else:
                break
        for i in range(1,8,1): # right
            if (position + i)%8 == 0:
                break
            elif (board[position +i] <19) and (board[position + i] >9):
                legalmoves = legalmoves + [position+i]
                break
            elif board[position+i] == 0:
                legalmoves = legalmoves + [position+i]
            else:
                break
        for i in range(1, 8, 1):  # left
            if position == 0:
                break
            if (position - i) % 8 == 7:
                break
            elif (board[position - i] < 19) and (board[position - i] > 9):
                legalmoves = legalmoves + [position - i]
                break
            elif board[position - i] == 0:
                legalmoves = legalmoves + [position - i]
            else:
                break
        for i in range(1,8,1): #backward left
            if position + 7*i > 63:
                break
            if (position+7*i)%8 == 7:
                break
            elif(board[position +7*i]) == 0:
                legalmoves = legalmoves + [position +7*i]
            elif ((board[position +7*i]) < 19) and ((board[position +7*i]) > 9):
                legalmoves = legalmoves + [position + 7*i]
                break
            else:
                break
        for i in range(1,8,1): #backward right
            if position + 9*i > 63:
                break
            if (position+9*i)%8 == 0:
                break
            elif(board[position +9*i]) == 0:
                legalmoves = legalmoves + [position +9*i]
            elif (board[position +9*i]) < 19 and (board[position +9*i]) > 19:
                legalmoves = legalmoves + [position + 9*i]
                break
            else:
                break
        for i in range(1,8,1): #forward left
            if position - 9*i <0:
                break
            if (position-9*i)%8 == 7:
                break
            elif(board[position -9*i]) == 0:
                legalmoves = legalmoves + [position -9*i]
            elif (board[position -9*i]) < 19:
                legalmoves = legalmoves + [position - 9*i]
                break
            else:
                break
        for i in range(1,8,1): #forward right
            if position - 7*i <0:
                break
            if (position-7*i)%8 == 0:
                break
            elif(board[position -7*i]) == 0:
                legalmoves = legalmoves + [position -7*i]
            elif (board[position -7*i]) < 19 and (board[position -7*i]) > 9:
                legalmoves = legalmoves + [position - 7*i]
                break
            else:
                break
    if board[position] == 25: # blackking
        for i in range(1,2,1): # backward
            if position + 8*i > 63:
                break
            elif board[position + 8*i] == 0:
                legalmoves = legalmoves + [position + 8*i]
            elif (board[position + 8*i] < 19) and (board[position + 8*i] > 9):
                legalmoves = legalmoves + [position + 8*i]
                break
            else:
                break
        for i in range(1, 2, 1):  # forward
            if position - 8*i < 0:
                break
            elif board[position - 8 * i] == 0:
                legalmoves = legalmoves + [position - 8 * i]
            elif (board[position - 8 * i] < 19) and (board[position - 8 * i] > 9):
                legalmoves = legalmoves + [position - 8 * i]
                break
            else:
                break
        for i in range(1,2,1): # right
            if (position + i)%8 == 0:
                break
            elif (board[position +i] <19) and (board[position + i] >9):
                legalmoves = legalmoves + [position+i]
                break
            elif board[position+i] == 0:
                legalmoves = legalmoves + [position+i]
            else:
                break
        for i in range(1, 2, 1):  # left
            if position == 0:
                break
            if (position - i) % 8 == 7:
                break
            elif (board[position - i] < 19) and (board[position - i] > 9):
                legalmoves = legalmoves + [position - i]
                break
            elif board[position - i] == 0:
                legalmoves = legalmoves + [position - i]
            else:
                break
        for i in range(1,2,1): #backward left
            if position + 7*i > 63:
                break
            if (position+7*i)%8 == 7:
                break
            elif(board[position +7*i]) == 0:
                legalmoves = legalmoves + [position +7*i]
            elif ((board[position +7*i]) < 19) and ((board[position +7*i]) > 9):
                legalmoves = legalmoves + [position + 7*i]
                break
            else:
                break
        for i in range(1,2,1): #backward right
            if position + 9*i > 63:
                break
            if (position+9*i)%8 == 0:
                break
            elif(board[position +9*i]) == 0:
                legalmoves = legalmoves + [position +9*i]
            elif (board[position +9*i]) < 19 and (board[position +9*i]) > 19:
                legalmoves = legalmoves + [position + 9*i]
                break
            else:
                break
        for i in range(1,2,1): #forward left
            if position - 9*i <0:
                break
            if (position-9*i)%8 == 7:
                break
            elif(board[position -9*i]) == 0:
                legalmoves = legalmoves + [position -9*i]
            elif (board[position -9*i]) < 19:
                legalmoves = legalmoves + [position - 9*i]
                break
            else:
                break
        for i in range(1,2,1): #forward right
            if position - 7*i <0:
                break
            if (position-7*i)%8 == 0:
                break
            elif(board[position -7*i]) == 0:
                legalmoves = legalmoves + [position -7*i]
            elif (board[position -7*i]) < 19 and (board[position -7*i]) > 9:
                legalmoves = legalmoves + [position - 7*i]
                break
            else:
                break
    return legalmoves

def IsPositionUnderThreat(board,position,player):
    if player == 10: #white under threat?
        if board[position] >19 or board[position]==0:
            print("White does not Occupy")
            return False
        for i in range (1,8,1): #rook or queen or king in front
            if position + 8*i >63:
                break
            if (board[position + 8*i] == 23) or (board[position + 8*i] == 24) or (board[position + 8] == 25):
                return True            
            if (board[position + 8*i] == 20) or (board[position + 8*i] == 21) or (board[position + 8*i] == 22):
                break
            if position+8*(i+1)<64 and board[position + 8*(i+1)] == 25:
                break
            if (board[position + 8*i] < 19) and (board[position + 8*i]) > 0:
                break
        for i in range (1,8,1): #rook or queen or king in back
            if position - 8*i <0:
                break
            if (board[position - 8*i] == 23) or (board[position - 8*i] == 24) or (board[position - 8] == 25):                
                return True  
            if (board[position - 8*i] == 20) or (board[position - 8*i] == 21) or (board[position - 8*i] == 22):
                break            
            if position-8*(i+1)>-1 and board[position - 8*(i+1)] == 25:
                break            
            if (board[position - 8*i] < 19) and (board[position - 8*i]) > 0:
                break            
        for i in range (1,8,1): #bishop or queen or king or pawn in front right
            if position + 9*i >63:
                break  
            if ((position)+9*i)%8 == 0:
                break
            if ((position)+9*i)%8 != 0: 
                if board[position +9*i] == 21 or board[position +9*i] == 23 or (board[position +9*i] <19 and board[position +9*i] > 0):
                    break
                if board[position +9*i] == 24 or board[position +9*i] == 22 or board[position +9] == 25 or board[position +9] == 20:
                    return True                
                if (position +(9*(i+1))) < 64 and board[position +(9*(i+1))] == 20 and (position +(9*(i+1)))%8 !=0: 
                    break
                if (position +(9*(i+1))) < 64 and board[position +(9*(i+1))] == 25 and (position +(9*(i+1)))%8 !=0: 
                    break                
        for i in range (1,8,1): #bishop or queen or king or pawn in front left
            if position + 7*i >63:
                break
            if ((position)+7*i)%8 == 7:
                break
            if ((position)+7*i)%8 != 7:
                if board[position +7*i] == 21 or board[position +7*i] == 23 or (board[position +7*i] <19 and board[position +7*i] > 0):
                    break
                if board[position +7*i] == 24 or board[position +7*i] == 22 or board[position +7] == 25 or board[position +7] == 20:
                    return True                
                if (position +(7*(i+1))) < 64 and board[position +(7*(i+1))] == 20 and (position +(7*(i+1)))%8 !=7:
                    break
                if (position +(7*(i+1))) < 64 and board[position +(7*(i+1))] == 25 and (position +(7*(i+1)))%8 !=7:
                    break                 
        for i in range (1,8,1): #bishop or queen or king in back left
            if position - 9*i <0:
                break  
            if ((position)-9*i)%8 == 7:
                break
            if ((position)-9*i)%8 != 7:
                if board[position -9*i] == 21 or board[position -9*i] == 23 or board[position -9*i] == 20:
                    break
                if (board[position -9*i] <19 and board[position -9*i] > 0):
                    break                 
                if board[position -9*i] == 24 or board[position -9*i] == 22 or board[position -9] == 25:
                    return True
                if (position -(9*(i+1))) >-1 and board[position -(9*(i+1))] == 25 and (position -(9*(i+1)))%8 !=7:
                    break                
        for i in range (1,8,1): #bishop or queen or king in back right   
            if position - 7*i <0:
                break           
            if ((position)-7*i)%8 == 0:
                break
            if ((position)-7*i)%8 != 0:
                if board[position -7*i] == 21 or board[position -7*i] == 23 or board[position -7*i] == 20:
                    break
                if (board[position -7*i] <19 and board[position -7*i] > 0):
                    break
                if board[position -7*i] == 24 or board[position -7*i] == 22 or board[position -7] == 25:
                    return True                
                if (position -(7*(i+1))) >-1 and board[position -(7*(i+1))] == 25 and (position -(7*(i+1)))%8 !=0:
                    break                 
        for i in range (1,8,1): #rook or queen or king on right
            if (position+i) > 63:
                break
            if (position+i) % 8 == 0:
                break
            if (board[position +i]) == 23 or (board[position +i]) == 24 or (board[position+1]) == 25:
                return True            
            if (board[position+i])<19 and (board[position+i])>0:
                break
            if (board[position+i])==20 or (board[position+i])==21 or (board[position+i])==22:
                break            
            if position+(i+1)<64 and(board[position+(i+1)])==25 and (position+i+1)%8!=0:
                break
        for i in range (1,8,1): #rook or queen or king on left
            if (position-i) < 0:
                break
            if (position-i) % 8 == 7:
                break
            if (board[position -i]) == 23 or (board[position -i]) == 24 or (board[position-1]) == 25:
                return True            
            if (board[position-i])<19 and (board[position-i])>0:
                break
            if (board[position-i])==20 or (board[position-i])==21 or (board[position-i])==22:
                break      
            if position-(i+1)>-1 and(board[position-(i+1)])==25 and (position-i-1)%8!=7:
                break            
        if (position+15)%8 != 7 and (position+15)<64 and board[position+15] == 21: #knight big forward left
            return True
        if (position+17)%8 != 0 and (position+17)<64 and board[position+17] == 21: #knight big forward right
            return True
        if (position+10)%8 != 0 and (position+10)%8 != 1 and (position+10)<64 and board[position+10] == 21: #knight small forward right
            return True   
        if (position+6)%8 != 7 and (position+6)%8 != 6 and (position+6)<64 and board[position+6] == 21: #knight small forward left
            return True
        if (position-10)%8 != 7 and (position-10)%8 != 6 and (position-10)>=0 and board[position-10] == 21: #knight small backward left
            return True
        if (position-6)%8 != 0 and (position-6)%8 != 1 and (position-6)>=0 and board[position-6] == 21: #knight small backward right
            return True
        if (position-17)%8 != 7 and (position-17)>=0 and board[position-17] == 21: #knight big backward left
            return True 
        if (position-15)%8 != 0 and (position-15)>=0 and board[position-15] == 21: #knight big backward right
            return True         
    if player == 20: #black under threat?
        if board[position] <19 or board[position]==0:
            print("Black does not Occupy")
            return False        
        for i in range (1,8,1): #rook or queen or king in back
            if position + 8*i >63:
                break
            if (board[position + 8*i] == 13) or (board[position + 8*i] == 14) or (board[position + 8] == 15):
                return True            
            if (board[position + 8*i] == 10) or (board[position + 8*i] == 11) or (board[position + 8*i] == 12):
                break
            if position+8*(i+1)<64 and board[position + 8*(i+1)] == 15:
                break            
            if (board[position + 8*i] > 19):
                break
        for i in range (1,8,1): #rook or queen or king in front
            if position - 8*i <0:
                break
            if (board[position - 8*i] == 13) or (board[position - 8*i] == 14) or (board[position - 8] == 15):
                return True 
            if position-8*(i+1)>-1 and board[position - 8*(i+1)] == 15:
                break           
            if (board[position - 8*i] > 19) or (board[position - 8*i] == 10) or (board[position - 8*i] == 11) or (board[position - 8*i] == 12):
                break            
        for i in range (1,8,1): #bishop or queen or king or pawn in back right
            if position + 9*i >63:
                break  
            if ((position)+9*i)%8 == 0:
                break
            if ((position)+9*i)%8 != 0: 
                if board[position +9*i] == 14 or board[position +9*i] == 12 or board[position +9] == 15:
                    return True                
                if board[position +9*i] == 11 or board[position +9*i] == 13 or board[position +9*i] >19 or board[position +9*i] == 10:
                    break
                if (position +(9*(i+1))) < 64 and board[position +(9*(i+1))] == 15 and (position +(9*(i+1)))%8 !=0: 
                    break                 
        for i in range (1,8,1): #bishop or queen or king in back left
            if position + 7*i >63:
                break               
            if ((position)+7*i)%8 == 7:
                break
            if ((position)+7*i)%8 != 7:
                if board[position +7*i] == 14 or board[position +7*i] == 12 or board[position +7] == 15:
                    return True                
                if board[position +7*i] == 11 or board[position +7*i] == 13 or board[position +7*i] >19 or board[position +7*i] == 10:
                    break 
                if (position +(7*(i+1))) < 64 and board[position +(7*(i+1))] == 15 and (position +(9*(i+1)))%8 !=7: 
                    break                
        for i in range (1,8,1): #bishop or queen or king or pawn in front left
            if position - 9*i <0:
                break  
            if ((position)-9*i)%8 == 7:
                break
            if ((position)-9*i)%8 != 7:
                if board[position -9*i] == 14 or board[position -9*i] == 12 or board[position -9] == 15  or board[position -9] == 10:
                    return True                
                if board[position -9*i] == 11 or board[position -9*i] == 13:
                    break
                if (board[position -9*i] >19):
                    break
                if position-(9*(i+1))>-1 and board[position -(9*(i+1))] == 10 and (position -(9*(i+1)))%8 !=7:
                    break
                if position-(9*(i+1))>-1 and board[position -(9*(i+1))] == 15 and (position -(9*(i+1)))%8 !=7:
                    break                
        for i in range (1,8,1): #bishop or queen or king or pawn in front right   
            if position - 7*i <0:
                break            
            if ((position)-7*i)%8 == 0:
                break
            if ((position)-7*i)%8 != 0:
                if board[position -7*i] == 11 or board[position -7*i] == 13:
                    break
                if board[position -7*i] == 14 or board[position -7*i] == 12 or board[position -7] == 15 or board[position -7] == 10:
                    return True                
                if (board[position -7*i] >19):
                    break
                if position-(7*(i+1))>-1 and board[position -(7*(i+1))] == 10 and (position -(7*(i+1)))%8 !=0:
                    break
                if position-(7*(i+1))>-1 and board[position -(7*(i+1))] == 15 and (position -(7*(i+1)))%8 !=0:
                    break                 
        for i in range (1,8,1): #rook or queen or king on right
            if (position+i) > 63:
                break
            if (position+i) % 8 == 0:
                break
            if (board[position +i]) == 13 or (board[position +i]) == 14 or (board[position+1]) == 15:
                return True            
            if (board[position+i])>19:
                break
            if (board[position+i])==10 or (board[position+i])==11 or (board[position+i])==12:
                break   
            if position+(i+1)<64 and(board[position+(i+1)])==15 and (position+i+1)%8!=0:
                break            
        for i in range (1,8,1): #rook or queen or king on left
            if (position-i) < 0:
                break
            if (position-i) % 8 == 7:
                break
            if (board[position -i]) == 13 or (board[position -i]) == 14 or (board[position-1]) == 15:
                return True            
            if (board[position-i])>19:
                break
            if (board[position-i])==10 or (board[position-i])==11 or (board[position-i])==12:
                break                 
            if position-(i+1)>-1 and(board[position-(i+1)])==15 and (position-i-1)%8!=0:
                break            
        if (position+15)%8 != 7 and (position+15)<64 and board[position+15] == 11: #knight big backward left
            return True
        if (position+17)%8 != 0 and (position+17)<64 and board[position+17] == 11: #knight big backward right
            return True
        if (position+10)%8 != 0 and (position+10)%8 != 1 and (position+10)<64 and board[position+10] == 11: #knight small backward right
            return True   
        if (position+6)%8 != 7 and (position+6)%8 != 6 and (position+6)<64 and board[position+6] == 11: #knight small backward left
            return True
        if (position-10)%8 != 7 and (position-10)%8 != 6 and (position-10)>=0 and board[position-10] == 11: #knight small forward left
            return True
        if (position-6)%8 != 0 and (position-6)%8 != 1 and (position-6)>=0 and board[position-6] == 11: #knight small forward right
            return True
        if (position-17)%8 != 7 and (position-17)>=0 and board[position-17] == 11: #knight big forward left
            return True 
        if (position-15)%8 != 0 and (position-15)>=0 and board[position-15] == 11: #knight big forward right
            return True         
    return False

def evalboard(board):
    boardval = 0
    for i in board:
        if i == 14:#whitequeen
            boardval = boardval + 20*5 
        elif i == 24:#blackqueen
            boardval = boardval - 20*5  
        elif i == 15:#whiteking
            boardval = boardval + 5000
        elif i == 25:#blackking
            boardval = boardval - 5000
        elif i == 10:#whitepawn
            boardval = boardval + 10
        elif i == 20:#blackpawn
            boardval = boardval - 10  
        elif i == 13:#whiterook
            boardval = boardval + 50
        elif i == 23:#blackrook
            boardval = boardval - 50
        elif i == 12:#whitebishop
            boardval = boardval + 30
        elif i == 22:#blackbishop
            boardval = boardval - 30
        elif i == 11:#whiteknight
            boardval = boardval + 30
        elif i == 21:#blackknight
            boardval = boardval - 30           
    return boardval

def newboard(board,oldpos,newpos):
    new=list(board)
    new[newpos] = new[oldpos]
    new[oldpos] = 0
    return new
class tree:
    def __init__(self,x):
        self.store = [x,[]]

    def AddSuccessor(self,x):
        self.store[1] = self.store[1] + [x]
        return True

    def Get_LevelOrder(self):
        lists=[]
        a=Queue()
        a.enqueue(self)
        while(a.empty() == False):
            r=a.dequeue()
            lists = lists + [r.store[0]]
            for i in r.store[1]:
                a.enqueue(i)
        print(lists)
        return lists
class Queue:
    def __init__(self):
        self.store=[]
    def enqueue(self,val):
        self.store = self.store + [val]
        return True
    def dequeue(self):
        r = self.store[0]
        self.store = self.store[1:len(self.store)]
        return r
    def empty(self):
        if self.store == []:
            return True
        elif self.store != []:
            return False

def chessPlayer(board,player):
    if player == 10:
        OGBoard = tree([])
        opp = 20
        oldpos=GetPlayerPositions(board,player)
        evaltree=[]#Player's moves and corresponding opponent's moves and values
        candidateMoves=[]#All player's moves
        evaltreelevelorder=[]#Holder to ensure evaltree is inlevelorder
        move = []
        for old in oldpos:
            newpos = GetPieceLegalMoves(board,old) #oldpos has all current positions, newpos has all new positions for each piece
            for new in newpos:
                child = tree([old,new,"score"])
                newbrd = newboard(board,old,new)
                veryoldpos = GetPlayerPositions(newbrd,opp)
                for veryold in veryoldpos:
                    verynewpos = GetPieceLegalMoves(newbrd,veryold)
                    for verynew in verynewpos:
                        verynewbrd = newboard(board,veryold,verynew)
                        grandchild = tree([veryold,verynew,evalboard(verynewbrd)])
                        evaltree = evaltree + [[[grandchild.store[0][0],grandchild.store[0][1]]] + [grandchild.store[0][2]]]
                        if child.store[0][2] == "score":
                            child.store[0][2] = grandchild.store[0][2]
                        elif child.store[0][2]>grandchild.store[0][2]:
                            child.store[0][2] = grandchild.store[0][2]
                OGBoard.AddSuccessor(child)
        OGBoard.store[0] = OGBoard.store[0] + [[OGBoard.store[1][0].store[0][0],OGBoard.store[1][0].store[0][1]]]
        OGBoard.store[0] = OGBoard.store[0] + [OGBoard.store[1][0].store[0][2]]
        for i in OGBoard.store[1]:
            if i.store[0][2]>OGBoard.store[0][1]:
                OGBoard.store[0][0] = [i.store[0][0],i.store[0][1]]
                OGBoard.store[0][1] = i.store[0][2]
        for i in OGBoard.store[1]:
            candidateMoves = candidateMoves + [[[i.store[0][0],i.store[0][1]]] + [i.store[0][2]]]
        for i in OGBoard.store[1]:
            evaltreelevelorder = evaltreelevelorder+[[[i.store[0][0],i.store[0][1]]] + [i.store[0][2]]]
        evaltree = evaltreelevelorder + evaltree
        move = OGBoard.store[0][0]
        for i in range(0,len(candidateMoves),1):
            candidateMoves[i][1] = float(candidateMoves[i][1])        
        return[True,move,candidateMoves,evaltree]
    elif player == 20:
        OGBoard = tree([])
        opp = 10
        oldpos=GetPlayerPositions(board,player)
        evaltree=[]
        candidateMoves=[]
        evaltreelevelorder=[]#Holder to ensure evaltree is inlevelorder
        for old in oldpos:
            newpos = GetPieceLegalMoves(board,old) #oldpos has all current positions, newpos has all new positions for each piece
            for new in newpos:
                child = tree([old,new,"score"])
                newbrd = newboard(board,old,new)
                veryoldpos = GetPlayerPositions(newbrd,opp)
                for veryold in veryoldpos:
                    verynewpos = GetPieceLegalMoves(newbrd,veryold)
                    for verynew in verynewpos:
                        verynewbrd = newboard(board,veryold,verynew)
                        grandchild = tree([veryold,verynew,evalboard(verynewbrd)])
                        evaltree = evaltree + [[[grandchild.store[0][0],grandchild.store[0][1]]] + [grandchild.store[0][2]]]
                        if child.store[0][2] == "score":
                            child.store[0][2] = grandchild.store[0][2]
                        elif child.store[0][2]<grandchild.store[0][2]:
                            child.store[0][2] = grandchild.store[0][2]
                OGBoard.AddSuccessor(child)
        OGBoard.store[0] = OGBoard.store[0] + [[OGBoard.store[1][0].store[0][0],OGBoard.store[1][0].store[0][1]]]
        OGBoard.store[0] = OGBoard.store[0] + [OGBoard.store[1][0].store[0][2]]
        for i in OGBoard.store[1]:
            if i.store[0][2]<OGBoard.store[0][1]:
                OGBoard.store[0][0] = [i.store[0][0],i.store[0][1]]
                OGBoard.store[0][1] = i.store[0][2]
        for i in OGBoard.store[1]:
            candidateMoves = candidateMoves + [[[i.store[0][0],i.store[0][1]]] + [i.store[0][2]]]
        for i in OGBoard.store[1]:
            evaltreelevelorder = evaltreelevelorder+[[[i.store[0][0],i.store[0][1]]] + [i.store[0][2]]]
        evaltree = evaltreelevelorder + evaltree
        move = OGBoard.store[0][0]
        for i in range(0,len(candidateMoves),1):
            candidateMoves[i][1] = float(candidateMoves[i][1])
        return[True,move,candidateMoves,evaltree]   
    else:
        return[False,[[]],[],[[]]]

###############################################################Player vs AI
done = False
while not(done):
    #White
    printlist(board)
    printboard(board)
    wkingmoves = []
    wpiecemoves = []
    wpiecesaveking = []
    for a in range(0,64,1):
        if board[a] == 15:
            whiteking = a
            break
    if IsPositionUnderThreat(board,whiteking,10) == True:
        print("Save your King!")
        wkinglegal = GetPieceLegalMoves(board,whiteking)
        for i in wkinglegal:
            pseudoboard = list(board)
            pseudoboard[whiteking] = 0
            pseudoboard[i] = 15
            if IsPositionUnderThreat(pseudoboard,i,10) == False:
                wkingmoves = wkingmoves + [i]
        for i in range(0,64,1):
            if board[i] >9 and board[i]<15:
                wpiecemoves = GetPieceLegalMoves(board,i)
                for b in wpiecemoves:
                    pseudoboard = list(board)
                    pseudoboard[i] = 0
                    pseudoboard[b] = board[i]
                    if IsPositionUnderThreat(pseudoboard,whiteking,10) == False:
                        wkingmoves = wkingmoves + [1]
        if len(wkingmoves) == 0:
            print("black wins")
            done = True
            break    
    while True:
        x = int(input("Player White Move, Piece Position "))
        y = int(input("Player White Move, Piece Future Position "))
        r = GetPieceLegalMoves(board,x)
        if (y not in r) or board[x]>15 or board[x]<9:
            print("Legal Move Please")
        elif y in r:
            break
    pseudoboard = list(board)
    pseudoboard[y] = pseudoboard[x]
    pseudoboard[x] = 0
    for a in range(0,64,1):
        if pseudoboard[a] == 15:
            whiteking = a
            break
    if IsPositionUnderThreat(pseudoboard,whiteking,10) == True:
        while IsPositionUnderThreat(pseudoboard,whiteking,10):
            print("save your king!")
            while True:
                x = int(input("Player White Move, Piece Position "))
                y = int(input("Player White Move, Piece Future Position "))
                r = GetPieceLegalMoves(board,x)
                if (y not in r) or board[x]>15 or board[x]<9:
                    print("Legal Move Please")
                elif y in r:
                    break
            pseudoboard = list(board)
            pseudoboard[y] = pseudoboard[x]
            pseudoboard[x] = 0
            if IsPositionUnderThreat(pseudoboard,whiteking,10) == False:
                break
    board[y] = board[x]
    board[x] = 0
            
    r = chessPlayer(board,20)
    board = list(newboard(board,r[1][0],r[1][1]))