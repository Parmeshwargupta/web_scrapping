def pattern(n):
    for i in range(n+1 ):
        for j in range(1,i+1):
            print(j,end="")
        print()    


n = int(input("Enter the number: "))
pattern(n)
