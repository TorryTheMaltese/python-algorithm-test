import sys

sys.stdin = open("in1.txt", "rt")


def dfs(v):
    global res, n, m,cnt
    if v==m:
        for i in res:
            print(i, end=' ')
        print()
        cnt = cnt+1
        return
    else:
        for i in range(1, n+1):
            res[v]=i
            dfs(v+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0]*m
    cnt=0
    dfs(0)
    print(cnt)
