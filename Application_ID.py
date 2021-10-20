def Number(n):
    if(n>26):
        p=[int(i) for i in str(n)]
        return Number(sum(p))
    else:
        return n

a= input()
p=[int(i) for i in a]
S=sum(p)
ans=Number(S)
print(chr(ans+64))            