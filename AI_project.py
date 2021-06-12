import sys

player_layout = [4,4,4,4,4,4,0]
ai_layout = [0,4,4,4,4,4,4]

def game_ends(Ai_side,Player_side):  ### is end

    if ((sum(Ai_side[1:7]))==0)or((sum(Player_side[0:6]))==0):

        if (sum(Ai_side[1:7])) == 0:

            Player_side[6] = Player_side[6]+sum(Player_side[0:6])
            Player_side[0:6] = [0, 0, 0, 0, 0, 0]

        else:

            Ai_side[0] = Ai_side[0] + sum(Ai_side[1:7])
            Ai_side[1:7] =[0,0,0,0,0,0]

        return True
    else:
        return False

def Final_score(Ai_side,Player_side):

   #if game_ends(Ai_side,Player_side):
        if Ai_side[0]>Player_side[6]:
            #print( 'Ai wins with final score '+(str(Ai_side[0]))+' ,player loses with final score '+(str(Player_side[6])))
            return 70

        if Ai_side[0] == Player_side[6]:
            #print( 'No winner with final score ' + (str(Ai_side[0])) + ' for each')
            return 0

        else:
            #print( 'player wins with final score ' + (str(Player_side[6]))+ ' ,Ai loses with final score ' + (str(Ai_side[0])))
            return -70

def experimental_score(Ai_side, Player_side):

    return (Ai_side[0]-Player_side[6])

#######################################################

def minimax_alphabeta(player_layout,AI_layout, alpha, beta, depth, is_Max,withstealing):
    if depth == 0:
        return experimental_score(AI_layout,player_layout), -1

    if game_ends(AI_layout, player_layout):
        return Final_score (AI_layout, player_layout), -1
    if is_Max:
        compared_value = -1000000
        move = -1
        for i in range(6, 0, -1):
            if AI_layout[ i ] == 0: continue
            x = AI_layout [:]
            y = player_layout [:]
            ismax = make_ai_move(i, x, y,withstealing);
            newleaf, _ = minimax_alphabeta(y,x, alpha, beta, depth - 1, ismax,withstealing)
            if compared_value < newleaf:
                move = i
                compared_value = newleaf
            alpha = max( compared_value,alpha)
            if alpha >= beta:  # the cutoff condition
                break
        return compared_value, move
    else:
        compared_value = 1000000
        move = -1
        for i in range(0, 6, 1):
            if player_layout[i] == 0: continue
            x = AI_layout [:]
            y = player_layout[:]
            ismax = make_player_move(i+1,y,x,withstealing);
            newleaf, _ = minimax_alphabeta(y,x, alpha, beta,depth - 1 , not ismax,withstealing)
            if compared_value > newleaf:
                move = i+1
                compared_value = newleaf
            beta = min(compared_value, beta)
            if alpha >= beta: # the cutoff condition
                break
        return compared_value , move

##########################################################


def make_player_move(n, player_layout, ai_layout,with_stealing = False):

        value = player_layout[n - 1]
        index = n - 1
        player_layout[index] = 0
        flag = True  # first time in player board
        while (value):
            if (flag):  # first time in player board
                for i in range(index + 1, 7):

                    if value == 1 and i < 6 and player_layout[i] == 0 and with_stealing and ai_layout[i+1] != 0 :
                        value -= 1
                        player_layout[6] = ai_layout[i+1]+1+player_layout[6]
                        ai_layout[i+1] = 0

                    else:
                        player_layout[i] += 1
                        value -= 1

                    if value == 0:
                        break
                if i == 6 and value == 0 and sum(player_layout[0:6])!=0:  # play again
                    return True

            else:  # second time in player board

                for i in range(0, 7):

                    if value == 1 and i<6 and player_layout[i] == 0 and with_stealing and ai_layout[i+1] != 0:
                        value -= 1
                        player_layout[6] = ai_layout[i+1] + 1 + player_layout[6]
                        ai_layout[i+1] = 0
                    else:
                        player_layout[i] += 1
                        value -= 1
                    if value == 0:
                        break
                if i == 6 and value == 0 and sum(player_layout[0:6])!=0:
                    return True

            if i == 6 and value != 0:  #player in ai
                for j in range(i, 0, -1):  # end value should be checked (1)
                    ai_layout[ j ] += 1
                    value -= 1
                    if value == 0:
                        break
                if j == 1 and value != 0:
                    flag = False
        return False


def make_ai_move(n, ai_layout, player_layout,with_stealing=False):
    value = ai_layout[ n ]
    index = n
    ai_layout[ index ] = 0
    flag = True  # first time in player board

    while (value):

        if (flag):  # first time in player board

            for i in range(index - 1, -1, -1):
                if value == 1 and i>0 and ai_layout[ i ] == 0 and with_stealing and player_layout[i - 1] != 0:
                    value -= 1
                    ai_layout[0] = player_layout[i - 1] + 1 + ai_layout[0]
                    player_layout[i - 1] = 0
                else:
                    ai_layout[ i ] += 1
                    value -= 1

                if value == 0:
                    break
            if i == 0 and value == 0 and sum(ai_layout[1:7])!=0:
                return True

        else:  # second time in player board

            for i in range(6, -1, -1):
                if value == 1 and i>0 and ai_layout[ i ] == 0 and with_stealing and player_layout[ i - 1 ] != 0:
                    value -= 1
                    ai_layout[ 0 ] = player_layout[ i - 1 ] + 1 + ai_layout[ 0 ]
                    player_layout[ i - 1 ] = 0
                else:
                    ai_layout[ i ] += 1
                    value -= 1
                if value == 0:
                    break
            if i == 0 and value == 0 and sum(ai_layout[1:7])!=0:
                return True

        if i == 0 and value != 0:
            for j in range(i, 6):  # end value should be checked (0 or 1)
                player_layout[ j ] += 1
                value -= 1
                if value == 0:
                    break
            if j == 5 and value != 0:
                flag = False

    return False


def player_move(player_layout):
    has_move = True
    while has_move:

        command = input("Player turn: ").split()
        if not command:
            continue
        if command[ 0 ] == "exit":
            sys.exit(0)
        c = int(command[ 0 ])

        while ( not(0<c<7) or player_layout[c-1]==0):
            command = input("Player turn: enter another number : ").split()
            if not command:
                continue
            if command[0] == "exit":
                sys.exit(0)
            c = int(command[0])
        if with_or_without == "1":
            has_move = make_player_move(c, player_layout, ai_layout, True)
        elif with_or_without == "0":
            has_move = make_player_move(c, player_layout, ai_layout, False)
        else:
            has_move = make_player_move(c, player_layout, ai_layout,)
        layout()
    return player_layout


def ai_move(ai_layout):
    has_move = True
    while has_move:
        #_,c = minimax_alphabeta(player_layout,ai_layout,-1000000,1000000,10,True)
        #print ("AI move ---> " + str(c))

        if with_or_without == "1":
            _, c = minimax_alphabeta(player_layout, ai_layout, -1000000, 1000000, depth, True,True)
            if c==-1:
                print("Game Ended")
                break
            print("AI move ---> " + str(c))
            has_move = make_ai_move(c, ai_layout, player_layout, True)
        elif with_or_without == "0":
            _, c = minimax_alphabeta(player_layout, ai_layout, -1000000, 1000000, depth, True,False)
            print("AI move ---> " + str(c))
            if c == -1:
                print("Game Ended")
                break
            has_move = make_ai_move(c, ai_layout, player_layout, False)
        else:
            _, c = minimax_alphabeta(player_layout, ai_layout, -1000000, 1000000, depth, True,False)
            print("AI move ---> " + str(c))
            if c == -1:
                print("Game Ended")
                break
            has_move = make_ai_move(c, ai_layout, player_layout,)
        layout()
    return ai_layout


def layout():
    print("          ----------------- ")
    print("         ", end="")
    print(*[ "%2d" % x for x in ai_layout[ 1:7 ] ], sep="|")
    print(
        "AI --> %2d ----------------- %2d <-- You"
        % (ai_layout[0],player_layout[6])
    )
    print("         ", end="")
    print(*[ "%2d" % x for x in player_layout[ 0:6 ] ], sep="|")
    print("          ----------------- ")
    print("")
    print("          ↑  ↑  ↑  ↑  ↑  ↑")
    print("moves:    1  2  3  4  5  6")

def playing_mode():
    global with_or_without
    global game_mode
    global depth
    layout()
    with_or_without = input(
        " choose mode enter 1 for with stealing and 0 for without stealing and defualt is without stealing \n")

    player_or_ai = input("who play first : enter 1 for player first , or 2 for ai first ")


    game_mode = input("enter 1 or 2 or 3  : 1-easy_mode ,2-medium_mode ,3-hard_mode ")
    if game_mode == "1":
        depth = 2
    if game_mode == "2":
        depth = 5
    if game_mode == "3":
        depth = 12
    while (1):
        if player_or_ai == "1":
            if game_ends(ai_layout,player_layout):
                break
            player_move(player_layout)
            if game_ends(ai_layout,player_layout):
                break
            ai_move(ai_layout)
        else:
            if game_ends(ai_layout,player_layout):
                break
            ai_move(ai_layout)
            if game_ends(ai_layout,player_layout):
                break
            player_move(player_layout)
    layout()

if __name__ == "__main__":
    play_another_game =True
    while (play_another_game):
        playing_mode()
        play_another_game=input("play_another_game? enter 1 for yes or 0 for no ")
        if (play_another_game=="1"):
            play_another_game = True
            player_layout = [ 4, 4, 4, 4, 4, 4, 0 ]
            ai_layout = [ 0, 4, 4, 4, 4, 4, 4 ]
        if(play_another_game=="0"):
            play_another_game =False
##################################################