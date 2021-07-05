import sys

# sys.stdin = open("in1.txt", "rt")


def dfs(v):
    global n, f,ch
    if v==n:
        if calc_triangle(res)==f:
            for r in res:
                print(r, end=' ')
            exit()
    else:
        for i in range(1, n+1):
            if ch[i]==0:
                res[v] = i
                ch[i]=1
                dfs(v+1)
                ch[i]=0
        return


def calc_triangle(arr):
    b = [1]*n
    total = 0

    for i in range(1, n):
        b[i] = (b[i-1]*(n-i))//i

    for j in range(n):
        total += arr[j]*b[j]
    return total


if __name__ == "__main__":
    n, f = map(int, input().split())
    res = [0]*n
    ch = [0]*(n+1)
    dfs(0)
