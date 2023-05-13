def alphabet(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(ord('a')+i),end='')
        print()        
n=int(input("Enter the number: "))
alphabet(n)  