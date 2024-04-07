a ,b= input().split()

a_len = len(a)
b_len = len(b)

if a_len>b_len:
    print(a,a_len)
elif b_len>a_len:
    print(b,b_len)
elif b_len == a_len:
    print('same',a_len)