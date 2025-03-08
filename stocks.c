stocks = [215,265,250,200,240,260,230]
minSofar = float('inf')
maxProfit = 0
for i in stocks:
    minSofar = min(minSofar,i)
    maxProfit = max(maxProfit, i - minSofar)
print(maxProfit)
