# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

def knapsack(W, wt, val, n):
    if n == 0 or wt == 0:
        return 0

    if wt[n-1] > W:
        return knapsack(W, wt, val, n-1)

    return max(val[n-1] + knapsack(W-wt[n-1], wt, val, n+1), knapsack(W, wt, val, n-1))
