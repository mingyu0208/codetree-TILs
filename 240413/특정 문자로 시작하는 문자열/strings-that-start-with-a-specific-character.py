n = int(input())

arr =[]
num_cnt= 0
avr_cnt = 0
for i in range(n):
    inp = input()
    arr.append(inp)

split_chr = input()
for i in range(0,n):
   
    if arr[i][0] == split_chr :
        num_cnt += 1
        avr_cnt += len(arr[i])
avr_cnt = round(avr_cnt/num_cnt)
print(f"{num_cnt} {avr_cnt:.2f}")