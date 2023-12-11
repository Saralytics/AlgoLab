# For example: a = 100, b = 200, the GCD is 100
# a = 7, b = 13, the GCD is 1
# a = 2, b = 6 , the GCD is 2 

# Thought process:
# The greatest common divisor must be smaller than or equal to the smaller number of a and b 
# suppose small = a 
# if b can be divided by a: then a is the GCD
# if not, we find the next divisor of a , until b can be divided 
# how to find the next divisor of a?


# My native implimentation : simple for loop

def gcd(a, b):
  if a >= b:
    a, b = b , a # the rest of the program assumes a is the smaller number
    
  if b % a == 0:
    return a
  for i in range(a-1, 0, -1):
    if a % i == 0 and b % i == 0:
      return i

# Euclidean algorithm
# Optimized euclidean algorithm


