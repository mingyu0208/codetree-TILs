n = int(input())

arr = [input() for _ in range(n)]
end= input()
cnt = 0
sum_val = 0

for i in range(n):
        for j in range(n):
            sum_val+=j

        if arr[i][0] == end:
            cnt+=1

avg = sum_val//n

print(f'{cnt} {avg:.2f}')