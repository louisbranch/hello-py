# Hello!

y = int(raw_input('Enter a number: '))
sqr = y * y

if sqr == 0:
  result = ' is Zero'
elif sqr % 2 == 0:
  result = ' is Even'
else:
  result = ' is Odd'

print(str(sqr) + result)
