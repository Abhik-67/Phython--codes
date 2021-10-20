def Number(n):
    s=0
    while n>0:
        rem=n%10
        s=s+rem
        n=n//10
    return(s)
n=int(input("apid::"))
st="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
r=Number(n)

while r>26:
    n=r
    r=Number(n)
if r==0:
    print(-1)
else:
    print(st[r-1])        