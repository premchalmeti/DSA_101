# https://www.geeksforgeeks.org/fractional-knapsack-problem/

class ItemValue:
    def __init__(self, v, w) -> None:
        self.v = v
        self.w = w
        self.ratio = v // w

    def __lt__(self, other):
        return self.ratio < other.ratio


def solve(vw_pairs, W):
    max_cost = 0

    ratios = [ItemValue(v, w) for (v, w) in vw_pairs]
    ratios.sort(reverse=True)

    for item in ratios:
        if (W - item.w) > 0:
            max_cost += item.v
            W -= item.w
        else:
            fraction = W / item.w
            max_cost += (item.v * fraction)
            W = int(W - (item.w * fraction))
            break
    return max_cost


if __name__ == '__main__':
    # (value, weight)
    vw_pairs = [(60, 10), (40, 40), (100, 20), (120, 30)]
    W = 50
    print(solve(vw_pairs, W))
