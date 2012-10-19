balance = 5000.00
annualInterestRate = 0.18
monthlyPaymentRate = 0.02
months = range(1,13)
monthlyInterestRate = 1 + annualInterestRate/12
totalPaid = 0.0

for month in months:
  minimumPayment = balance * monthlyPaymentRate
  totalPaid += minimumPayment
  remaining = balance - minimumPayment
  newBalance = remaining * monthlyInterestRate
  balance = newBalance

  print('Month: ' + str(month))
  print('Minimum monthly payment: ' + str(round(minimumPayment,2)))
  print('Remaining balance: ' + str(round(balance,2)))

print('Total paid: ' + str(round(totalPaid,2)))
print('Remaining balance: ' + str(round(balance,2)))
