import math

def f(x):
  return  1/(x**2) # 1/x² dx

def compositeTrapezoidal(a, b, n):
  x0 = a
  xn = b
  h = (b - a)/n

  xi = []

  for i in range(1, int((b-a)/h)):
    xi.append(a + (i*h))

  print(xi)
  # (f(x0) + f(x1)) * (h/2)
  return (f(x0) + 2*sum([f(i) for i in xi]) + f(xn)) * (h/2)

a = 1
b = 7
n = 329

print(round(compositeTrapezoidal(a, b, n), 4))
