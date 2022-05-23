import sys

result = []

count = int(input())

for i in range(count):
    tmp = list(map(str, sys.stdin.readline().split()))

    k = float(tmp[0])
    for j in range(len(tmp) - 1):
        if tmp[j + 1] == '@':
            k *= 3
        elif tmp[j + 1] == '%':
            k += 5
        elif tmp[j + 1] == '#':
            k -= 7

    result.append(k)

for i in range(len(result)):
    print("{:.2f}".format(result[i]))

