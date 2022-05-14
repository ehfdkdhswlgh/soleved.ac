import sys

intList = []

for i in range(9):
    intList.append(int(sys.stdin.readline()))

print("{0}\n{1}".format(max(intList), intList.index(max(intList)) + 1))