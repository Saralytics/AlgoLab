"""Clarification of the notation:
Big O notation, strictly speaking represent the higher bound,
so any runtime that is higher or equal to the actual runtime
can be expressed by Big O. In interviews, usually we are asked
to find the Big O notation that is close to the actual runtime,
which is a definition closer to Big Theta Notation - the exact
bound. For familiarity, I'm still going to use Big O Notation
for the exercises.
"""

# 1st Example
# 1.1 while loop
i = 0
n = 100
c = 2
while i < n:
    i += c
# solution:
# 0 + 2 + 4 + 6 ... < n
# ceil(n/c) -> O (n) -> linear time

# 1.2 equivalent for loop
for i in range(0, n, c):
    i = i + c
# time complexity is the same as above

# 2nd Example
n = 32
i = 1
c = 2
while i < n:
    i = i * c
# solution:
# 1, 2, 4, 8, 16 ... n -> 2**k < n
# k = log(2)n -> O(logn) -> logn time

# 3rd Example
n = 32
c = 2
while n > 1:
    n = n / c

# solution:
# 2**4, 2**3, 2**2, 2**1, 2**0 -> log(2)n > 1
# O(logn)

# 4th Example
i = 2
c = 2
while i < n:
    i = i ** c
# solution:
# 2, 2**c, (2**c)**c, ((2**c)**c)**c, ..., (2**c)**k <n
# c**k < log(2)n
# k < log(c)log(2)n
# O(log logn)

# 5th Exmaple - subsequent loops
i = 0
while i < n:
    i += 2
i = 1
while i < n:
    i *= 3
while i < 100:
    i += 1
# solution:
# The first loop: O(n) + the second loop O(logn) + the third loop O(1)
# remove the lower order terms -> we are left with O(n)

# 6th Example - nested loops
i = 0
j = 1
while i < n:
    while j < n:
        j *= 2
    i += 1

# solution
# inner loop O(logn) * outer loop O(n) -> O (n * logn)


# 6th Example - mixed loops
i = 1
j = 2
while i < n:
    while j < n:
        j *= 2
    i += 1
while i < n:
    while j < n:
        j += 1
    i += 1
# solution
# O(logn)*O(n) + O(n)*O(n) -> O(n*logn)+O(n**2)
# ignore the lower order terms, we are left with O(n**2)


# 7th example - mixed input
i = 1
j = 2
m = 200 # some user input
while i < n:
    while j < n:
        j *= 2
    i += 1
while i < m:
    while j < m:
        j += 1
    i += 1

# solution:
# O(n*logn) + O(m**2)
# since there are 2 different input independent of each other,
# do not ignore either: O(nlogn + m**2)


