def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(ord('A')+i),end='')
        print()    
n=int(input("Enter the number: ")) 

pattern2(n)