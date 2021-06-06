import sys


# sys.stdin = open("in1.txt", "rt")


def dfs(v, sum_result, tsum):
    global sum_max
    if sum_result > c:
        return
    if sum_result + (total - tsum) < sum_max:
        return
    if v > n:
        if sum_max < sum_result <= c:
            sum_max = sum_result
        return
    else:
        dfs(v + 1, sum_result + ba_duks[v], tsum + ba_duks[v])
        dfs(v + 1, sum_result, tsum + ba_duks[v])


if __name__ == "__main__":
    c, n = map(int, input().split())
    ba_duks = []
    for _ in range(n):
        ba_duks.append(int(input()))
    res = 0
    ba_duks.insert(0, 0)
    sum_max = 0
    total = sum(ba_duks)
    dfs(1, 0, 0)
    print(sum_max)
