# hackerrank: https://www.hackerrank.com/challenges/sparse-arrays/

def matchingStrings(strings, queries):
    from collections import Counter
    cache = Counter(strings)
    return [cache[q] for q in queries]


if __name__ == '__main__':
    strings = ["aba", "baba", "aba", "xzxb"]
    queries = ["aba", "xzxb", "ab"]
    print(matchingStrings(strings, queries))

