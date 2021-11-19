'''
HACKEREARTH PROBLEM:

Maximum partition

You are given an array A consisting of Nintegers. You can make any number of partitions in the array such
that when you combine all these partitions, the value of the special sum that is obtained is maximum. 
If you make K partitions in the array, then the special sum is defined as P1-P2+P3-P4+Pg...+(-1)^(K-1)Pk. Here Pi 
is defined as the summation of all the integers in that partition.

Task:
Determine the maximum special sum that can be obtained. Note Assume 1 Based Indexing.

Assumptions:
N=3
A= [1,2,3]

Approach:
You can have K = 3 partitions. So, P₁=1, P2=-2, P3=3
The sum obtained is P1 P2 + P3-1-(-2) +3=6.

Input:
3
[1,-2,3]
Output:
6

Input:



'''

N=int(input())
arr=list(map(int,input().split(" ")))
print(arr[0]+sum(abs(i) for i in arr[1:]))