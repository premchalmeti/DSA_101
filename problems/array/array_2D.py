# hackerrank: https://www.hackerrank.com/challenges/2d-array/problem

# [r-1][c-1] [r-1][c] [r-1][c+1]
#            [r][c]
# [r+1][c+1] [r+1][c] [r+1][c+1]

def calc_hsum(mat, r, c):
    return sum(
        (
            mat[r-1][c-1], mat[r-1][c], mat[r-1][c+1], 
            mat[r][c], 
            mat[r+1][c+1], mat[r+1][c], mat[r+1][c+1]
        )
    )


def solve(mat):
    N = len(mat)
    return max(
        [calc_hsum(mat, r, c) for r in range(1, N-1) for c in range(1, N-1)]
    )


if __name__ == "__main__":
    mat1 = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(solve(mat1))

    mat2 = [
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    print(solve(mat2))
