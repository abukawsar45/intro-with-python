# print('Assalamualaikum')

# ----- task - 1 ---------------------------
product = 1150

if(product>1000):
  discount=(product/100)*15
  priceWithoutDiscount=product - discount
  print(f'total price without discount: {priceWithoutDiscount}')

else:
    print(f'total price: {product} and no discount')

# ----- task - 2  ---------------------------
# lets fix we want to buy 2 liter of mojo and the minimum price is the
four_500ml = 4 * 35
two_1000ml = 2 * 60
one_2000ml = 1 * 100
if(four_500ml>two_1000ml):
    if(one_2000ml>two_1000ml):
      print(f'we are buy two bottle mojo at price: {two_1000ml} tk')
    else:
      print(f'we are buy one bottle mojo at price: {one_2000ml} tk')
elif(one_2000ml>four_500ml):
      print(f'we are buy four bottle mojo at price: {four_500ml} tk')
   
else:   
   print(f'we are buy one bottle mojo at price: {one_2000ml} tk')
   


# ----- task - 3 ---------------------------
celsius = 15
kelvin = celsius + 273.15
print(f'kelvin is: {kelvin}')

# ----- task - 4 ---------------------------
totalSeat = 240
totalCostPerHour = 18600
perSeatCost = totalCostPerHour / totalSeat

targetProfit = 2000
profitWithCostPerHour= totalCostPerHour + targetProfit
paySinglePassenger = profitWithCostPerHour / totalSeat

print(f'Per Seat Cost: {perSeatCost} USD')
print(f'Per Seat bill: {paySinglePassenger:.2f} USD')



# ----- task - 5 ---------------------------
firstFriend = 20
secondFriend = 50
thirdFriend = 30

total = firstFriend + secondFriend + thirdFriend
# print(total)
average = total/3
print(f'average: {average:.2f}')