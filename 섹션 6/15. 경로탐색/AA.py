import sys


# sys.stdin = open("in1.txt", "r")


def dfs(v):
    global cnt, ch
    if v == n:
        cnt += 1
    else:
        ch[v] = 1
        for i in range(1, n + 1):
            if arr[v][i] == 1 and ch[i] == 0:
                dfs(i)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    ch = [0] * (n + 1)
    cnt = 0

    for _ in range(m):
        a, b = map(int, input().split())
        arr[a][b] = 1

    dfs(1)
    print(cnt)
