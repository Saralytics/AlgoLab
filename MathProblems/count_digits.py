# for example we have n = 9876, the count of digits of n is 4
# write a function to find the number of digits of a given integer
def count_digits(n):
  counter = 0
  while n > 0:
    n = n//10
    counter += 1
  return counter
    
