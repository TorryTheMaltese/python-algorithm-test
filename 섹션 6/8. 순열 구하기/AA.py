import sys

# sys.stdin = open("in1.txt", "rt")


def dfs(v):
    global res, cnt, ch
    if v==m:
        for r in res:
            print(r, end=' ')
        print()
        cnt = cnt+1
        return
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                res[v]=i
                ch[i]=1
                dfs(v+1)
                ch[i]=0
        return


if __name__ == "__main__":
    n,m = map(int, input().split())
    res = [0]*m
    ch = [0]*(n+1)
    cnt = 0
    dfs(0)
    print(cnt)
