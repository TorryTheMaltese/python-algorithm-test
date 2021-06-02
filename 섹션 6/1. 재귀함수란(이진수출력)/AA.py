import sys

# sys.stdin = open("in1.txt", "rt")


def print_decimal_to_binary(x):
    if x == 0:
        return
    else:
        print_decimal_to_binary(x // 2)
        print(x % 2, end=' ')


if __name__ == "__main__":
    n = int(input())
    print_decimal_to_binary(n)
