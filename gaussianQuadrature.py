import math
# n = 2 points
a = 1
b = 5

def f(x):
  return (2*(x**3)) + (3*(x**2)) + (6*x) + 1 # 2x³ + 3x² + 6x + 1

def F(t):
   return (( b - a )/2) * f(x(t))

def x(t):
  return ((( b - a )/2)*t) + (( a + b)/2)

def gaussianQuadrature():
  return F(-1/math.sqrt(3)) + F(1/math.sqrt(3))

print(round(gaussianQuadrature(), 4))
