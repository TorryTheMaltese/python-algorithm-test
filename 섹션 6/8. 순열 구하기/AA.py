import sys

# sys.stdin = open("in1.txt", "rt")


def dfs(v):
    global res, arr, cnt
    if v > m:
        for i in range(1,v):
            print(res[i], end=" ")
        print()
        cnt += 1
        return
    else:
        for i in range(1, n+1):
            if arr[i] == 0:
                arr[i] = 1
                res[v]=i
                dfs(v+1)
                arr[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    arr = [0]*(n+1)
    res = [0]*n
    dfs(1)
    print(cnt)
