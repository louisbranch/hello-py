balance = 3329
annualInterestRate = 0.2

months = range(1,13)
monthlyInterestRate = 1 + annualInterestRate/12

mountlyIncrease = balance * annualInterestRate/12

minimumPayment = mountlyIncrease - (mountlyIncrease % 10)

while ( True ):

    testBalance = balance

    for month in months:
      remaining = testBalance - minimumPayment
      testBalance = remaining * monthlyInterestRate

    if remaining < 0:
      break

    minimumPayment += 10

print('Lowest Payment: ' + str(int(minimumPayment)))
