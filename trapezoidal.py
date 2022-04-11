import math

def f(x):
  return (x**2) * (math.e**(-x))  # x^2e^-x dx

def trapezoidal(a, b):
  x0 = a
  x1 = b
  h = b - a

  # (f(x0) + f(x1)) * (h/2)
  return (f(x0) + f(x1)) * (h/2)

a = 0
b = 1

print(round(trapezoidal(a, b), 4))
