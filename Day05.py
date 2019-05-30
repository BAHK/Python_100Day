import math

def PerfectNumber(num):
    sum = 0
    k = num
    j = 0
    for j in range( 1 , k ):
        if k % j == 0:
            sum += j
            if sum == k :
                print(" %d   is a PerfectNumber")

max_num = int(input('请输入最大范围 :'))
for num in range( 2 , max_num ):
    PerfectNumber( max_num )



"""
#include "stdio.h"
void main()
{
int j,k,sum = 0;
for(k=2;k<=1000;k++)
{
sum=0;
for(j=1;j<k;j++)
if(k%j==0)
sum=sum+j;
if(sum==k)
printf("%d ",k);
}
}
"""
