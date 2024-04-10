string = input()
cnt_str = input()
cnt = 0

for i in string:
    if i in cnt_str:
        cnt+=1
print(cnt)