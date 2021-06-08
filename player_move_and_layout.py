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

