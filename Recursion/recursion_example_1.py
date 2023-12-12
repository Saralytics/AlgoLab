# 1. What does the below function print? Draw out the execution order
def fun(n):
  if n == 0:
    return
  print(n)
  fun(n-1)
  print(n)
fun(3)
# answer: 3, 2, 1, 1, 2, 3

# 2. What does the below function print?
def fun(n):
  if n == 0:
    return
  fun(n-1)
  print(n)
  fun(n-1)

fun(3)
# answer: 1, 2, 1, 3, 1, 2, 1


# 3. What does the below function do?
def fun(n):
  if n <= 1:
    return 0
  else:
    return fun(n//2)

fun(16)
# answer: 4 
# This function finds the log2N of input n


# 4. What does the below function do?
def fun(n):
  if n <= 0:
    return
  fun(n//2)
  print(n%2)

fun(13)
# answer: 1, 1, 0, 1
# prints the binary representation of input n
  
