s1 = input()
s2 = input()
s3 = input()

leng1, leng2, leng3 = len(s1), len(s2), len(s3)

arr = leng1, leng2, leng3 

print(max(arr)- min(arr))