itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00
#calculate profit, saleprice as 25% deducted from retailprice,saleprofit
profit = retailPrice - wholesalePrice
salePrice = retailPrice - (retailPrice * 0.25)
saleProfit = salePrice - wholesalePrice

print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(profit))
print("Sale Price: $" + str(salePrice))
print("Sale Profit: $" + str(saleProfit))