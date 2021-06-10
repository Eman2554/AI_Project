def make_ai_move(n, ai_layout, player_layout,with_stealing=False):

    value = ai_layout[n] #index corresponding entered bocket no. checked to be vslid before function calling
    index = n
    ai_layout[index] = 0 #make it empty
    flag = True  # first time in ai board wen first calling the function

    while (value): #looping over ai-side bockets then player_side bockets till all balls are moved

        if (flag):  # first time in ai board

            for i in range(index - 1, -1, -1):
                if with_stealing and value == 1 and i>0 and ai_layout[ i ] == 0 and player_layout[i - 1] != 0: #with stealing handler
                    value -= 1
                    ai_layout[0] = player_layout[i - 1] + 1 + ai_layout[0]
                    player_layout[i - 1] = 0
                else:#witout stealing or stealing conditions aren't fullfilled
                    ai_layout[ i ] += 1
                    value -= 1

                if value == 0:
                    break
            if i == 0 and value == 0 and sum(ai_layout[1:7])!=0: #play again handler
                return True

        else:  # second time in ai board (not first time)

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
            if i == 0 and value == 0 and sum(ai_layout[1:7])!=0: # play again handler
                return True

        if i == 0 and value != 0:
            for j in range(i, 6): #accessing player side except it's score
                player_layout[ j ] += 1
                value -= 1
                if value == 0:
                    break
            if j == 5 and value != 0: #more balls so acess ai-side (not first tome)
                flag = False

    return False