import sys

# sys.stdin = open("in1.txt", "rt")

first = list(input())
second = list(input())


def check_anagram(first_word, second_word):
    for alphabet in second_word:
        if alphabet in first_word:
            first_word.remove(alphabet)
        else:
            return False
    if len(first_word) == 0:
        return True


if check_anagram(first, second):
    print("YES")
else:
    print("NO")
