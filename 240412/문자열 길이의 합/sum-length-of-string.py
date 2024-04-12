n = int(input())

arr = [
    input()
    for _ in range(n)
]
cnt = 0
a_sum = 0

    

for i in arr:
    for elem in i:
        if elem in 'a':
            a_sum+=1
    for j in i:
        cnt+=1

print(f'{cnt} {a_sum}')