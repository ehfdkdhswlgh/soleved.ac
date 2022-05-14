
A = int(input())
B = int(input())
C = int(input())

result = A * B * C
result_str = str(result)

countArr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(result_str)):
    for j in range(0, len(countArr)):
        if int(result_str[i]) == j:
            countArr[j] += 1

for i in range(len(countArr)):
    print(countArr[i])
