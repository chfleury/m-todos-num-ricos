import math

def f(x):
  return  1/(x**2) # 1/x² dx


def compositeSimpsons13(a, b, n):
  x0 = a
  xn = b
  h = (b - a)/n

  xe = [] # even
  xo = [] # odd

  for i in range(1, int((b-a)/h)):
    if i % 2:
        xo.append(a + (i*h))
    else:
        xe.append(a + (i*h))


  print(xo, xe)
  return (f(x0) + 2*sum([f(i) for i in xe]) + 4*sum([f(i) for i in xo]) + f(xn)) * (h/3)


a = 1
b = 7
n = 10

print(round(compositeSimpsons13(a, b, n), 4))
