N = 3


def get_mat():
    global mat

    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]


def rot_mat():
    for i in range(N/2):
        for j in range(i, N-i-1):
            aux = mat[i][j]

            mat[i][j] = mat[j][N-i-1]
            mat[j][N-i-1] = mat[N-i-1][N-j-1]
            mat[N-i-1][N-j-1] = mat[N-j-1][i]
            mat[N-j-1][i] = aux


def print_mat():
    for row in mat:
        for col in row:
            print col,
        print ""


if __name__ == '__main__':
    get_mat()
    print "Before rotation,"
    print_mat()

    rot_mat()

    print "After rotatation,"
    print_mat()
