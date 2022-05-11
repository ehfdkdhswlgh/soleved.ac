# 문제
# 16진수 수를 입력받아서 10진수로 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 16진수 수가 주어진다. 이 수의 최대 길이는 6글자이다. 16진수 수는 0~9와 A~F로 이루어져 있고, A~F는 10~15를 뜻한다. 또, 이 수는 음이 아닌 정수이다.
#
# 출력
# 첫째 줄에 입력으로 주어진 16진수 수를 10진수로 변환해 출력한다.


inputStr = input()
inputStrLength = len(inputStr)
result = 0


# range([start,] stop [,step])

k = 0

for i in range(inputStrLength, 0, -1):
    ch = inputStr[k]
    if ch >= '1' and ch <= '9':
        result += int(inputStr[k]) * (16 ** (i - 1))
    elif ch >= 'A' and ch <= 'F':
        j = ord(ch) - 55
        result += j * (16 ** (i - 1))
    k = k + 1
print(result)