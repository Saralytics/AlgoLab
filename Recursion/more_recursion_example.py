# 1. Print 1 to N using recursion
# I: n = 4
# O: 1, 2, 3, 4

def fun1(n):
  if n < 1:
    return
  fun1(n-1)   # it's important here we put the recursive call before the print, because we are printing from 1 to n
  print(n)

## COMPARE WITH THE BELOW

# 2. Print N to 1 using recursion
# I: n = 5
# O: 5, 4, 3, 2, 1

def fun2(n):
  if n < 1:
    return
  print(n)
  fun1(n-1)   

# 3. Sum of digits using recursion
# I/p: 253
# O/p: 10 (2 + 5 + 3)

def recursive_sum(n):
  if n//10 <= 1:
    return n
  return recursive_sum(n//10) + n%10


# 4. Check if a string is palindrome using recursion
def is_palindrome(str:str, start:int, end:int):
  if start >= end:
    return true
  return str[start] == str[end] and is_palindrome(str, start+1, end -1)
