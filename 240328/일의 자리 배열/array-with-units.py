# arr = int(input().split())
a,b = list(map(int,input().split()))
arr = [a,b]
# arr.append(a)
# arr.append(b)

for i in range(2,10):
    arr.append((arr[i - 2] + arr[i - 1]) % 10)

for elem in arr:
    print(elem,end= " ")