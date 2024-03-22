n = int(input())
new_list = [1,n]
cnt = 1


while True:
    cnt+=1
    new_list.append(new_list[cnt - 1] + new_list[cnt - 2])
    if new_list[cnt]>100:
        break
for elem in new_list:
    print(elem,end=" ")