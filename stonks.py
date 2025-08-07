# Write code below 💖
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]
def price_at(x):
  print(stock_prices[x-1])
def max_price(a,b):
  for i in range(stock_prices[a+1], stock_prices[b]):
    print(max(stock_prices[i]))
def min_price(a,b):
   for i in range(stock_prices[a+1], stock_prices[b]):
     print(min(stock_prices[i]))


x = int(input("enter the price you want for that day:"))
a = int(input("enter the inital day you want :"))
b = int(input("enter the final day you want:"))
price_forday = price_at(x)
print("price for that day:", price_forday)
maxp = max_price(a,b)
print("Max price at that day:", maxp)
minp = min_price(a,b)
print("Min price at that day:", minp)