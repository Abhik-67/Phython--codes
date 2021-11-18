'''
TCS PROBLEM NQT 2021:
For the given a String 'S' of length 'N' consists of stream of character not in predefined order. Write a program
to find the second non repeating character in a string S.

Input: gaahaajapsps

Output: h

Explanation: in the given string 'gaahaajapsps'. There are 3 non repeating characters (g, h, j) in the string. 
As per problem statement we have to print the 2nd non-repeating character, hence the output in 'h'.
'''

'''
s= input()      #gaahaajapsps
n= len(s)
new = ""
if n >30:
    print("Wrong Input")
else:
    for i in s:
        if s.count(i) == 1:
            if i not in new:
                new= new+i
            else:
                continue
    if len(new)>1:
        print(new[1])       #h
    else:          
        print("Invalid Input")    
'''  

n= input()
l= []
for i in range(len(n)):
    if n[i] not in n[:i] and n[i] not in n[i+1:]:
        l.append(n[i])
if len(l)<2:
    print("Invalid String")
else:
    print(l[1])            