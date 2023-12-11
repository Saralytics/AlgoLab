# factorial of 1 is 1, factorial of 0 is 1
# factorial of n = 1*2*3*...*n, n must be >= 0
# There are 2 ways to solve this: iteratively or recursively

def factorial_iterative(n):
  if n == 1 or n == 0:
    print(f"The result is 1")
  else: 
    result = 1
    for i in range(2, n+1):
      result *= i
    print(f"The result is {result}")



def factorial_recursive(n):
  if n == 1 or n == 0:
    return 1
  return n * factorial_recursive(n-1)
    
