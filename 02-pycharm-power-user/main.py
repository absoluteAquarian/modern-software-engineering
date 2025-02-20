def print_board(board: list[list[str]]) -> None:
    """
    Prints the current state of the Tic-Tac-Toe game board
    :param board: The game board represented as a jagged 2D list of strings
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def has_player_won(board: list[list[str]], player: str) -> bool:
    """
    Checks if any vertical, horizontal or diagonal line has 3 marks for the
    given player
    :param board: The game board represented as a jagged 2D list of strings
    :param player: The icon for the player, either X or O
    """
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board: list[list[str]]) -> bool:
    """
    Checks if the board is completely full of player marks
    :param board: The game board represented as a 2D jagged list of strings
    """
    return all(column != " " for row in board for column in row)


def play_the_game() -> None:
    """
    Plays one round of Tic-Tac-Toe
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    print("Tic-Tac-Toe Game")
    print_board(board)
    for turn in range(9):
        player = players[turn % 2]
        place_mark_for_player(board, player)
        print_board(board)
        if has_player_won(board, player):
            print(f"P {player} wins!")
            return
        if is_board_full(board):
            print("Draw!")
            return
    print("Draw!")

# Method extracted from play_the_game()
def place_mark_for_player(board: list[list[str]], player: str) -> None:
    """
    Requests a coordinate on the board to place a mark for the given player,
    and places it if the space is empty
    :param board: The game board represented as a jagged 2D list of strings
    :param player: The icon for the player, either X or O
    """
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


play_the_game()
