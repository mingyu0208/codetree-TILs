[a_age, a_gdr] = input().split()
[b_age, b_gdr] = input().split()

if (int(a_age)>=19 and str(a_gdr)=="M") or (int(b_age)>=19 and str(b_gdr)=="M"):
    print(1)
else:
    print(0)