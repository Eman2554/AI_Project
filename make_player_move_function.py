def make_player_move(n, player_layout, ai_layout, with_stealing=False):
    value = player_layout[n - 1]
    index = n - 1
    player_layout[index] = 0
    flag = True  # first time in player board
    while (value):
        if (flag):  # first time in player board
            for i in range(index + 1, 7):

                if value == 1 and i < 6 and player_layout[i] == 0 and with_stealing and ai_layout[i + 1] != 0:
                    value -= 1
                    player_layout[6] = ai_layout[i + 1] + 1 + player_layout[6]
                    ai_layout[i + 1] = 0

                else:
                    player_layout[i] += 1
                    value -= 1

                if value == 0:
                    break
            if i == 6 and value == 0 and sum(player_layout[0:6]) != 0:  # play again
                return True

        else:  # second time in player board

            for i in range(0, 7):

                if value == 1 and i < 6 and player_layout[i] == 0 and with_stealing and ai_layout[i + 1] != 0:
                    value -= 1
                    player_layout[6] = ai_layout[i + 1] + 1 + player_layout[6]
                    ai_layout[i + 1] = 0
                else:
                    player_layout[i] += 1
                    value -= 1
                if value == 0:
                    break
            if i == 6 and value == 0 and sum(player_layout[0:6]) != 0:
                return True

        if i == 6 and value != 0:  # player in ai
            for j in range(i, 0, -1):  # end value should be checked (1)
                ai_layout[j] += 1
                value -= 1
                if value == 0:
                    break
            if j == 1 and value != 0:
                flag = False
    return False
