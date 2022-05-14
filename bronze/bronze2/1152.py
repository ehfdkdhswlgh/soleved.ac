
str = input().strip()

arr_list = list(str.split())

if len(arr_list) == 0:
    print(0)
else:
    print(len(arr_list))