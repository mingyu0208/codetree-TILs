import decimal
a,b = map (int,input().split())
one =a
two = b

print(f"{(decimal.Decimal(str(one))/two):.21f}")