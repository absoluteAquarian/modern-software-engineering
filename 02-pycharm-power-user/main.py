def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def has_player_won(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(b):
    return all(c != " " for r in b for c in r)


def play_the_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_board(board)
    for turn in range(9):
        player = players[turn % 2]
        while 1:
            # noinspection PyBroadException
            try:
                row, column = map(int, input(f"P {player}, row col (0-2): ").split())
                if board[row][column] == " ":
                    board[row][column] = player
                    break
                else:
                    print("Nope. Again.")
            except:
                print("Wrong. 0-2 pls.")
        print_board(board)
        if has_player_won(board, player):
            print(f"P {player} wins!")
            return
        if is_board_full(board):
            print("Draw!")
            return
    print("Draw!")


play_the_game()
