# https://leetcode.com/discuss/interview-question/1226093/maximise-dumbbell-pairs


def taskOfPairing(freq):
    pairs = []
    pair_freq_cnt = {}

    for i in range(len(freq)):
        w = i+1
        f = freq[i]

        pair_cnt = f//2
        rem = f%2
        pairs.append([w, w]*pair_cnt)
        if rem:
            if pair_freq_cnt.get(w+1, 0) > 0:
                pairs.append([w, w+1])
                pair_freq_cnt[w+1] -= 1
            elif pair_freq_cnt.get(w-1, 0) > 0:
                pairs.append([w, w-1])
                pair_freq_cnt[w-1] -= 1
            else:
                pair_freq_cnt[w] = rem
    
    return pairs

# same approach but dint worked
def taskOfPairing(freq):
    count = 0
    marker = False
    for i in freq:
        if i != 0:
            count += i // 2
        if i % 2 != 0 and marker:
            count += 1
            marker = False
        elif i % 2 != 0:
            marker = True
        else:
            marker = False
    return count


if __name__ == '__main__':
    freq_weights = [3, 5, 4, 3]

    print(taskOfPairing(freq_weights))
