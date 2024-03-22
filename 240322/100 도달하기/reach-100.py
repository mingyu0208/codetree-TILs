n = int(input())
new_list = []

new_list.append(1)
new_list.append(n)

for i in range(2,10):
    new_list.append(new_list[i-1]+ new_list[i-2])
    
for elem in new_list:
    if elem > 100:
        print(elem,end=" ")
        break
    print(elem,end=" ")