# name of student: nevin
# number of student:990773785
# purpose of program: return in coins
# function of program:return in coins
# structure of program: Asking how much you have to pay and how much you already paid and then return the other remaining coins

toPay = int(float(input('Amount to pay: '))* 100) #
paid = int(float(input('Paid amount: ')) * 100) #
change = paid - toPay #

if change > 0: #
  coinValue = 500 #
  
  while change > 0 and coinValue > 0: #
    nrCoins = change // coinValue #

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #

# comment on code below:
    if coinValue == 500:
      wg1 = nrCoinsReturned
      coinValue = 200
    elif coinValue == 200:
      wg2 = nrCoinsReturned
      coinValue = 100
    elif coinValue == 100:
      wg3 = nrCoinsReturned
      coinValue = 50
    elif coinValue == 50:
      wg4 = nrCoinsReturned
      coinValue = 20
    elif coinValue == 20:
      wg5 = nrCoinsReturned
      coinValue = 10
    elif coinValue == 10:
      wg6 = nrCoinsReturned
      coinValue = 5
    elif coinValue == 5:
      wg7 = nrCoinsReturned
      coinValue = 2
    elif coinValue == 2:
      wg8 = nrCoinsReturned
      coinValue = 1
    else:
      wg9 = nrCoinsReturned
      coinValue = 0

print("Geld bonnetje")
print("----------------------------------------------------------------")
print(f"Je hebt {wg1} stuks van 500 cent gebruikt.")
print(f"Je hebt {wg2} stuks van 200 cent gebruikt.")
print(f"Je hebt {wg3} stuks van 100 cent gebruikt.")
print(f"Je hebt {wg4} stuks van 50 cent gebruikt.")
print(f"Je hebt {wg5} stuks van 20 cent gebruikt.")
print(f"Je hebt {wg6} stuks van 10 cent gebruikt.")
print(f"Je hebt {wg7} stuks van 5 cent gebruikt.")
print(f"Je hebt {wg8} stuks van 2 cent gebruikt.")
print(f"Je hebt {wg9} stuks van 1 cent gebruikt.")
print("----------------------------------------------------------------")
if change > 0: #
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')