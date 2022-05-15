import sys
count = int(input())

for i in range(count):
    R, S = sys.stdin.readline().split()
    R = int(R)

    for j in range(len(S)):
        for k in range(R):
            print(S[j], end='')
    print()