def solve(a: list) -> int:
    ans = 0
    for i in range(len(a)):
        ans += a[i]
    return ans

lst = [1, 2, 3, 4, 5]
print(solve(lst))
