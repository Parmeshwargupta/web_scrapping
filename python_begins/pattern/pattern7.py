def pattern(n):
    res=[]
    for i in range(n):
        x=i+1
        s=""
        for j in range(i+1):
            s=s+str(x)
            x+=1
        res.append(s)
    return res        

       


n = int(input("Enter the number: "))
s=pattern(n)
for i in s:
    print(i)

