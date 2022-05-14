import sys

N = int(input())

# 시간 초과!!!!
# for i in range(N):
#     A, B = map(int, input().split())
#     print(A + B)


# 반복된 입력을 받을 때 시간을 줄이기 위해선 sys.stdin.readline()을 사용 한다!
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
