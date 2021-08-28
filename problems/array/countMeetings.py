
def count_meetings(a, d, n):
    meeting_mat = []

    max_no_days = max(d)

    for i in range(n):
        meeting_mat.append([0] * max_no_days)

        for j in range(a[i], d[i]+1):
            meeting_mat[i][j-1] = 1

    count_meetings = 0

    for inv in range(n):
        if sum(meeting_mat[inv]) == 1:
            count_meetings += 1

    return count_meetings

if __name__ == '__main__':
    n = 3

    a = [1, 1, 2]
    d = [1, 2, 2]

    print(count_meetings(a, d, n))
