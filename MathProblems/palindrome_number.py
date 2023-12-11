# palindrome number is a number that is the same read from right to left or left to right
# example: 12321, 78987, 6
# write a function to check if an input number n is a palindrome number
# hint: construct a new number by traverse through the last digit

def palindrome(n):
  reverse = 0
  last_digit = 0
  tmp = n
  while tmp > 0:
    last_digit = tmp % 10
    print(f"last digit is{last_digit}" )
    reverse = reverse * 10 + last_digit
    print(f"reverse is {reverse}")
    tmp = tmp//10
    print(f"{tmp}")
  print(n == reverse)

