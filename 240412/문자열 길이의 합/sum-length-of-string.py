n = int(input())

arr = [
    input()
    for _ in range(n)
]
cnt = 0
a_sum = 0

for i in range(n):
    cnt += len(arr[i])
    if arr[i][0] == 'a':
        a_sum+=1
print(f'{cnt} {a_sum}')