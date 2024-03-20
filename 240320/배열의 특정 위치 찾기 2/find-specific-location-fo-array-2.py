arr = list(map(int,input().split()))

n  = len(arr)
sum_odd = 0
sum_even= 0

for i in range(n):
    if i%2==1:
        sum_odd+=arr[i]
    if i%2==0:
        sum_even+=arr[i]
if sum_even>sum_odd:
    print(sum_even-sum_odd)

if sum_even<sum_odd:
    print(sum_odd-sum_even)