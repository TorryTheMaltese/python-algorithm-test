import sys

# sys.stdin = open("in1.txt", "rt")


def dfs(v):
    global n, m, cnt
    if v > m:
        for j in range(1,m+1):
            print(res[j], end=' ')
        cnt+=1
        print()
        return
    else:
        for i in range(1, n + 1):
            res[v]=i
            dfs(v+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * (m + 1)
    cnt = 0
    dfs(1)
    print(cnt)
