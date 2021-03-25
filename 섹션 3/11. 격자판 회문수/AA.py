# import sys
# sys.stdin = open("in2.txt", "rt")

arr = [list(map(int, input().split())) for _ in range(7)]

# print("\n".join(" ".join(map(str, l)) for l in arr))

res = 0


def row_check(row_res):
    for i in range(7):
        for j in range(3):
            if arr[i][j] == arr[i][j + 4] and arr[i][j + 1] == arr[i][j + 3]:
                row_res += 1
    return row_res


def column_check(col_res):
    for i in range(3):
        for j in range(7):
            if arr[i][j] == arr[i + 4][j] and arr[i + 1][j] == arr[i + 3][j]:
                col_res += 1
    return col_res


res = row_check(res) + column_check(res)

print(res)
