# import sys
#
# sys.stdin = open("in1.txt", "rt")

sdoku = [list(map(int, input().split())) for _ in range(9)]


def row_check(arr):
    one_to_nine = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for i in range(9):
        if set(arr[i]) == one_to_nine:
            return True
    return False


def column_check(arr):
    one_to_nine = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for i in range(9):
        tmp = [arr[j][i] for j in range(9)]
        if set(tmp) == one_to_nine:
            return True
    return False


def board_check(arr):
    one_to_nine = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    dx = [1, 4, 7]
    dy = [1, 4, 7]
    for x in dx:
        for y in dy:
            tmp = list()
            tmp.append(arr[x - 1][y - 1])
            tmp.append(arr[x - 1][y])
            tmp.append(arr[x - 1][y + 1])
            tmp.append(arr[x][y - 1])
            tmp.append(arr[x][y])
            tmp.append(arr[x][y + 1])
            tmp.append(arr[x + 1][y - 1])
            tmp.append(arr[x + 1][y])
            tmp.append(arr[x + 1][y + 1])
            if set(tmp) != one_to_nine:
                return False
    return True


if row_check(sdoku) and column_check(sdoku) and board_check(sdoku):
    print("YES")
else:
    print("NO")

# print('\n'.join(' '.join(map(str, num)) for num in sdoku))
