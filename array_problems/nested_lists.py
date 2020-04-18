
def get_second_student_recs(student_recs):
    f, s = float('inf'), float('inf')
    sl_names = []
    fl_names = []

    for (score, names) in student_recs.items():
        if score < f:
            s = f
            f = score
            sl_names = fl_names
            fl_names = names
        elif score < s and score != f:
            s = score
            sl_names = names

    return sl_names


if __name__ == '__main__':
    """n = int(input())
    student_rec = {}

    for _ in range(n):
        name = str(input())
        score = str(input())
        if score not in student_rec:
            student_rec[score] = []
        student_rec[score].append(name)"""
    student_rec = {
        37.21: ["Harry", "Berry"],
        37.2: ["Tina"],
        41: ["Akriti"],
        39: ["Harsh"]
    }
    print(get_second_student_recs(student_rec))

