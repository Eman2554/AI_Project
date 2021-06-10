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