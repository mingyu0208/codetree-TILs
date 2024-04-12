arr =["apple", "banana", "grape", "blueberry", "orange"]
oneText = input()
cnt = 0

for i in range(len(arr)):
   if arr[i][2] == oneText or arr[i][3] == oneText:
    print(arr[i])
    cnt+=1
print(cnt)