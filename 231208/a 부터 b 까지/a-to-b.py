a,b = map(int,input().split())

a_st = a
b_ed = b


while a_st<=b_ed:
        if a_st%2==1:
            print(a_st,end=' ')
            a_st*=2
        else:
            print(a_st,end=' ')
            a_st+=3