VOWES = 'aeiou'

def count_subs(string, substring):
    count = 0
    start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count


def _calc_score(const, string):
    processed = set()
    score = 0

    s = string.index(const)
    e = s

    while e < len(string):
        substring = string[s: e+1]

        if substring not in processed:
            processed.add(substring)
            score += count_subs(string, string[s: e+1])
            print(substring, count_subs(string, string[s: e+1]))

        e += 1

    return score


def calc_stuart(string):
    dist_consts = {c for c in string if c.lower() not in VOWES}
    return sum(map(lambda c: _calc_score(c, string), dist_consts))


def calc_kevin(string):
    dist_vows = {c for c in string if c.lower() in VOWES}
    return sum(map(lambda c: _calc_score(c, string), dist_vows))


def minion_game(string):
    # stuart_score = calc_stuart(string)
    kevin_score = calc_kevin(string)

    # if stuart_score == kevin_score:
    #     print('Draw')
    # elif stuart_score > kevin_score:
    #     print(f'Stuart {stuart_score}')
    # else:
    #     print(f'Kevin {kevin_score}')


if __name__ == '__main__':
    minion_game('BANANA')
