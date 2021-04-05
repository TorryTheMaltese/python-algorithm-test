# import sys
#
# sys.stdin = open("in5.txt", "rt")

k, n = map(int, input().split())
arr = list(int(input()) for i in range(k))
maximum_line = max(arr)


def find_maximum_length_line(lt, rt, result):
    # print(f"lt: {lt}, rt: {rt}, result: {result}")
    tmp = (lt + rt) // 2
    count_num = count_line(tmp)
    if lt > rt:
        # print(f"return {result}")
        return result
    else:
        if count_num < n:
            return find_maximum_length_line(lt, tmp - 1, result)
        else:
            return find_maximum_length_line(tmp + 1, rt, tmp)


def count_line(max_len):
    count_result = 0
    for line in arr:
        count_result += line // max_len
    return count_result


res = find_maximum_length_line(1, maximum_line, 0)
print(res)
