
def queen_can_be_placed(chess_board, r, c):
    # check row till col
    for i in range(c):
        if chess_board[r][i] == 1:
            return False

    # check left upper diagonal
    for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
        if chess_board[i][j] == 1:
            return False

    # check left lower diagonal
    for i, j in zip(range(r, len(chess_board), 1), range(c, -1, -1)):
        if chess_board[i][j] == 1:
            return False

    return True


def place_queens(chess_board, N, c):
    if c == N:
        return True

    for r in range(N):
        if queen_can_be_placed(chess_board, r, c):
            chess_board[r][c] = 1

            if place_queens(chess_board, N, c+1):
                return True

            # backtrack
            chess_board[r][c] = 0

    return False


def init_board(N):
    return [[0 for _ in range(N)] for _ in range(N)]


def print_board(chess_board):
    for row in chess_board:
        for col in row:
            print(col, end=' ')
        print()


if __name__ == '__main__':
    N = 4

    chess_board = init_board(N)

    if not place_queens(chess_board, N, 0):
        print('Solution doesn\'t exists')
        exit(0)

    print_board(chess_board)
