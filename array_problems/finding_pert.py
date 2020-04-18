
def get_std_pert(student_rec, std_name):
    if std_name not in student_rec:
        return -1
    return sum(student_rec[std_name])/len(student_rec[std_name])


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(get_std_pert(student_marks, query_name))
