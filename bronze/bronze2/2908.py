A, B = input().split()

A_list = []
B_list = []

for i in range(3):
    A_list.append(int(A[i]))
    B_list.append(int(B[i]))

A_list.reverse()
B_list.reverse()

A_reverse = int(''.join(map(str, A_list)))
B_reverse = int(''.join(map(str, B_list)))

if A_reverse > B_reverse:
    print(A_reverse)
else:
    print(B_reverse)
