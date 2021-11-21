'''
David loved Numbers.He would like to segregate number based on below conditions.
1) A number is a Positive number which has 0 present in it.
2) A number with only leading zeros will not be considered.
if above 2 conditions satisfied.He will call it as "Valid Number". otherwise "Invalid Number".

Example:
1] Input->808086  Output-> Valid Number
2] Input->0013    Output-> Invalid Number
3] Input->654     Output-> Wrong Input(If Input value is out of range(not in between 0 and 10000)print wrong input)
4]Input->1000001  Output-> Invalid Number
'''
'''
num= input()
if  num[0] != '0' and int(num) >=1 and '0' in num[1:len(num):] and int(num) <=1000000:
    print("Valid Number")
elif int(num) >1000000:
    print("Wrong Input")
else:
    print("Invalid Number")       
'''

n=int(input())
if(n>1000000):
    print("Wrong Input")
else:
    n=str(n)
    if (n[0]=='0'):
        print("Invalid Number")
    elif(n.find('0')==-1):
        print("Invalid Number")
    else:
        print("Valid Number")            
