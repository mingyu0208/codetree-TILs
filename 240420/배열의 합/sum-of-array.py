import sys
input = sys.stdin.readline
n = 4
for _ in range(n):
    arr = list(map(int, input().split()))
    
    sum_val = sum(arr)
    print(sum_val)