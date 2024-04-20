n = int(input())

import sys
input = sys.stdin.readline


for i in range(n):
    a,b = map(int,input().split())
    sum_val = 0
    for elem in range(a,b+1):
        if elem%2==0:
            sum_val+=elem
    print(sum_val)