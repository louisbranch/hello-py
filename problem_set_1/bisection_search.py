balance = 3329
annualInterestRate = 0.2

months = range(1,13)
monthlyInterestRate = annualInterestRate/12

upperBound = (balance * (1 + monthlyInterestRate)**12)/12
lowerBound = balance/12

while ( True ):

    testBalance = balance
    minimumPayment = (upperBound + lowerBound) / 2

    for month in months:
      remaining = testBalance - minimumPayment
      testBalance = remaining * (1 + monthlyInterestRate)

    if remaining < -0.01:
      upperBound = minimumPayment
    elif remaining > 0.01:
      lowerBound = minimumPayment
    else:
      break

print('Lowest Payment: ' + str(round(minimumPayment,2)))
