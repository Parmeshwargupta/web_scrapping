def pattern(n):
    s = 'A'

    for i in range(n):
        print(s)
        s =chr(ord('B')+i)
           


n = int(input("Enter the number: "))
pattern(n)
