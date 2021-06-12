import sys

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

    playing_mode()

##################################################