import sys

# sys.stdin = open("in1.txt", "r")


def dfs(v, s):
    global cnt
    if v==m:
        for r in res:
            print(r, end=' ')
        print()
        cnt += 1
        return
    else:
        for i in range(s,n+1):
            res[v]=i
            dfs(v+1,i+1)
            res[v]=0


if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0]*m
    cnt = 0
    dfs(0, 1)
    print(cnt)
