import sys

lst = []

#방법1 중복을 허용하지 않는 set 자료형을 사용한다.
# for i in range(10):
#     lst.append(int(sys.stdin.readline()) % 42)
#
# my_set = set(lst)
# print(len(my_set))


#방법2 반복문을 사용한다
for i in range(10):
    j = int(sys.stdin.readline()) % 42
    if j not in lst:
        lst.append(j)

print(len(lst))
