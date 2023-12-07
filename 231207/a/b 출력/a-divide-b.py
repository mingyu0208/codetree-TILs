# import decimal
a,b = map (int,input().split())
one =a
two = b




print(f"{one//two}.",end="")

for i in range(20):
    one*=10
    print(one//two,end="")
    one%=two

# print(f"{(decimal.Decimal(str(one))/two):.20f}")