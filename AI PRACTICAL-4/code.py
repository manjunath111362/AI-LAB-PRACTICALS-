import math
# Display the board
def display_board(board):
    print()
    for i in range(0, 9, 3):
        print(" " + board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("---+---+---")
    print()

# Check winner
def check_winner(board):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


# Minimax with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    result = check_winner(board)

    # Terminal state
    if result == "O":
        return 10 - depth

    if result == "X":
        return depth - 10

    if result == "Draw":
        return 0

    # Maximizing player O
    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"

                score = minimax(
                    board,
                    depth + 1,
                    False,
                    alpha,
                    beta
                )

                board[i] = " "

                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                # Alpha-Beta pruning
                if beta <= alpha:
                    break

        return best_score

    # Minimizing player X
    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"

                score = minimax(
                    board,
                    depth + 1,
                    True,
                    alpha,
                    beta
                )

                board[i] = " "

                best_score = min(best_score, score)
                beta = min(beta, best_score)

                # Alpha-Beta pruning
                if beta <= alpha:
                    break

        return best_score


# Find best move for computer
def best_move(board):
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(
                board,
                0,
                False,
                -math.inf,
                math.inf
            )

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


# Main program
board = [" "] * 9

print("TIC-TAC-TOE")
print("You are X")
print("Computer is O")

print("Positions:")
print(" 1 | 2 | 3")
print("---+---+---")
print(" 4 | 5 | 6")
print("---+---+---")
print(" 7 | 8 | 9")

display_board(board)

while True:

    # Human move
    try:
        position = int(input("Enter position (1-9): ")) - 1
    except ValueError:
        print("Invalid input. Enter a number from 1 to 9.")
        continue

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid move. Try again.")
        continue

    board[position] = "X"
    display_board(board)

    result = check_winner(board)

    if result:
        if result == "Draw":
            print("Game Draw!")
        else:
            print(result, "wins!")
        break

    # Computer move
    print("Computer is thinking...")

    move = best_move(board)

    if move == -1:
        print("Game Draw!")
        break

    board[move] = "O"
    display_board(board)

    result = check_winner(board)

    if result:
        if result == "Draw":
            print("Game Draw!")
        else:
            print(result, "wins!")
        break
