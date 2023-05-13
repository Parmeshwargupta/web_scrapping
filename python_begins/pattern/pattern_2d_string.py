def pattern(n):
    res = [[] for k in range((n))]
    for i in range(n):
        ans = ''
        for j in range(i+1):
            if j == 0 or i == j:
                ans = ans + "1"
            else:
                ans = ans + "2"
        res[i].append(ans)
    return res


n = int(input("Enter the number: "))
print(pattern(n))
result = pattern(n)
for i in result:
    print(i)
