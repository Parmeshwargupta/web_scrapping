def pattern(n):
    s = '1'
    for i in range(n):
        print(s)
        s = s+'1'


n = int(input("Enter the number: "))
pattern(n)
