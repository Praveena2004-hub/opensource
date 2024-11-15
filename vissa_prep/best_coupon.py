x=int(input().strip())
price1=x-(x*0.10)
price2=x-100
final_price=min(price1,price2)
print(int(final_price))
