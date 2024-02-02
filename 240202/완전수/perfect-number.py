arr = input().split()

start = int(arr[0])
end = int(arr[1])

cnt = 0
val =0

for i in range(start+1,end):
    val = 0
    for j in range(1,i):
        if i%j ==0:
            val +=j
    if val == i:
        cnt +=1

print(cnt)