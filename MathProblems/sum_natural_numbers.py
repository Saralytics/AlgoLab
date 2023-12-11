# Sum a series of natural numbers
# sum(1,2,3,4,....,n)
def sum(n):
  """ sums the natural numbers ranging from 1 to n"""
  return n*(n+1)/2
  # or return n*(n+1)//2 floor division to get an integer value

# Time complexity: O(1) because only 1 calculation is needed, no matter how big n is
  
