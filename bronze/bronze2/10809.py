txt = list(input())
result = []

for i in range(ord('a'), ord('z') + 1):
    if chr(i) in txt:
        result.append(txt.index(chr(i)))
    else:
        result.append(-1)


for i in range(len(result)):
    print(result[i], end=' ')