def pattern2(n):
    for i in range(n+1):
        for j in range(n-i):
            print(j+1,end='')
        print()    
n=int(input("Enter the number: ")) 

pattern2(n)