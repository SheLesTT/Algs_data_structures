n, dollars = map(int,input().split())
prices = list(map(int,input().split()))

max_price =0
for price in prices:
    if max_price < price <= dollars:
        max_price = price
print(max_price)