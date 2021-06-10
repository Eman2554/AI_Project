def Final_score(Ai_side,Player_side):

        if Ai_side[0]>Player_side[6]: # AI wins the player
            return 70

        if Ai_side[0] == Player_side[6]: #draw
            return 0

        else:  # player wins AI
            return -70
