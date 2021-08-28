
def count_max_char(text):
    freq_cnt = {}

    for ch in text:

        if ch not in freq_cnt:
            freq_cnt[ch] = 0

        freq_cnt[ch] += 1

    return max(freq_cnt, key=freq_cnt.get)


if __name__ == "__main__":
    name = "aabcddaeq"
    print count_max_char(name)
