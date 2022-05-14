import sys

N = int(input())

for i in range(N):
    str = sys.stdin.readline()

    sum = 0
    weight = 0
    for k in range(len(str)):
        if str[k] == 'O':
           weight += 1
           sum += weight
        elif str[k] == 'X':
            weight = 0

    print(sum)