import math

def f(x):
  return (x**2) * (math.e**(-x))  # x^2e^-x 
  
def simpsons13(a, b):
  x0 = a
  x2 = b
  x1 = (x0 + x2)/2
  h = (b - a)/2

  # (f(x0) + f(x1)) * (h/2)
  return (h/3)*( f(x0) + 4*(f(x1)) + f(x2) ) 

a = 0
b = 1
 
print(round(simpsons13(a, b), 4))