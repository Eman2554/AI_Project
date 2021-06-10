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
