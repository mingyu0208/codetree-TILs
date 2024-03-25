a,b = list(map(int, input().split()))

arr = [a,b]
for i in range(2,10):
    arr.append(2 * arr[i-2] + arr[i-1])

for elem in arr:
    print(elem,end= " ")