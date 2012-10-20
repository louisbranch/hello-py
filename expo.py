def iterPower(base, exp):
  ans = base
  if exp == 0:
    return 1.00

  for i in range(1,exp):
    ans = ans * base
  return ans

def recurPower(base, exp):
  if exp == 0:
    return 1.00

  return base * recurPower(base, exp-1)

def recurPowerNew(base, exp):
  if exp == 0:
    return 1.00

  if exp % 2 == 0:
    return recurPowerNew(base*base, exp/2)
  else:
    return base * recurPowerNew(base, exp-1)

def gdcIter(a,b):
  m = min(a,b)
  while ( a % m != 0 or b % m != 0 ):
    m -= 1
  return m

def gdcRecur(a,b):
  m = min(a,b)
  x = max(a,b)
  if m == 0:
    return x
  return gdcRecur(m, x % m)

def lenRecur(aStr):
  if aStr == '':
    return 0
  return 1 + len(aStr[1:])

def isIn(char, aStr):

  if len(aStr) == 0:
    return False
  elif len(aStr) == 1:
    return char == aStr

  middleLen = len(aStr) / 2
  middleChar = aStr[middleLen]

  if char == middleChar:
    return True
  if char < middleChar:
    return False or isIn(char, aStr[0:middleLen])
  else:
    return False or isIn(char, aStr[middleLen:])
