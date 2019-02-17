def sum(n):
    sum=0
    x=1
    while x<=n:
        sum=sum+x
        x=x+1
    return sum
    
    

n1=sum(10)
n2=sum(100)
n3=sum(200)

res=n1+n2+n3

print(res)