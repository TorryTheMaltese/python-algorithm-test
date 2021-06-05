import sys

# sys.stdin = open("in4.txt", "rt")


def dfs(v):
    if v > n:
        return False
    else:
        sum0 = 0
        sum1 = 0
        for i in range(1, n + 1):
            if check[i] == 0:
                sum0 += arr[i]
            if check[i] == 1:
                sum1 += arr[i]
        if (sum0 != 0 and sum1 != 0) and sum0 == sum1:
            print("YES")
            sys.exit(0)

        check[v] = 1
        dfs(v + 1)
        check[v] = 0
        dfs(v + 1)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    check = [0] * (n + 1)
    if not dfs(1):
        print("NO")
