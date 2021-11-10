'''
AMAZON RECRUTEMENT HACKEREARTH PROBLEM:

Minimum addition
You are given a positive integer N.
You have to divide the number Ninto two numbers P1 and P2 such that:
• Each digit of N should belong to exactly one of P1 or one of P2 and this, in turn, would
utilize every digit of the number N.
• Form the numbers P1 and ply in a manner such that their sum is minimum.

Task
Determine the minimum possible sum of P1 and P2
Note: The order of occurrence of the digits in P1 and P2 may differ from the order of occurrence
of the digits in N.
Example
Assumption
• N = 4325
Approach
• P1 can be 25
• P2 can be 34
• The minimum sum of P1 and P2 is 59
. Note there are other possibilities of Pland P2 like 143, 25). (3. 245). 153. 24). etc but their
sum is not minimum
. Thus the answer is 59
Function description
Complete the function solve provided in the editor. This function takes the
following parameter and returns the required answer:
• N: Represents the positive integer
Input format
Note: This is the input format that you must use to provide custom input (available above the
Compile and Test button).
• The first line contains I denoting the number of test cases. T also specifies the number of
times you have to run the solve function on a different set of inputs.
• For each test case:
o The first line contains an integer N.
Output format
♡
For each test case, print the minimum possible sum of the two numbers P1 and P2.
Constraints
1ST < 105
10 <N<2* 1018
Code snippets (also called starter code/boilerplate code)
This question has code snippets for C, CPP, Java, and Python.
Explanation
The first line contains the number of test cases, T = 2
The first test case
This is the same as the example Please refer to that.
The second test case
Given
• N = 867
Approach
• P1 can be 68
• P2 can be 7
• Minimum sum of P1 and P2 is 75
. Note there are other possibilities of P1 and P2 also like (6 78). (6. 87), etc but their sum is not
minimum
Thus the answer is 75

'''

def minAddition(N):
    list=[]
    for i in str(N):
        list.append(int(i))
    list.sort()
    sum1,sum2=0,0
    for i in range(len(list)):
        if i%2==0:
            sum1=sum1*10+list[i]
        else:
            sum2=sum2*10+list[i]    
    return sum2+sum1

T = int(input())
for _ in range(T):
    N= int(input())

    out_ = minAddition(N)
    print(out_)

'''
Input:-
7
4325            #Output:- 59
867             #Output:- 75 
4891            #Output:- 67   
8732            #Output:- 65
9008            #Output:- 17
516             #Output:- 21
4755            #Output:- 102
'''
