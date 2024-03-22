n = int(input())
cnt = 0

new_list =[]
new_list.append(n)

for i in range(1,10):
    a = new_list[i-1] + new_list[0]
    new_list.append(a)

for elem in new_list:
    print(elem, end=" ")
    if elem%5==0:
        cnt+=1
    if cnt>=2:
        break