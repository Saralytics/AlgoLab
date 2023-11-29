# Using the tree method
# 1. Identify the Base Case: Determine the base case of the recursion,
# which is the condition where the recursion stops. The base case typically takes constant time
# Understand the Recurrence Relation: Analyze how the function calls itself.
# The number of recursive calls and how the problem size changes with each call are key.
# This step is about understanding the pattern of recursion.
# 2. Express as a Recurrence Relation:
# Formulate the time complexity as a recurrence relation.
# For example, if a function makes two recursive calls with half the problem size each time, the relation might be
# T(n)=2T(n/2)+f(n), where f(n) represents the time taken for non-recursive work in each call.
# 3. Solve the Recurrence Relation:
# Recursion Tree Method:
# This involves drawing a tree representing the recursive calls,
# calculating the cost at each level, and then summing these costs.

# Example 1: write the recurrence relation for the below and analyze the time complexity
def fun(n):
    if n == 1:
        return
    print("Hello")  # constant regardless of n
    fun(n / 2)

# Solution:
# Recurrence relation: when n > 1 -> t(n) = t(n/2) + c; when n == 1 -> O(1)
# Use Recurrence Tree to find the time complexity
# 1st c
#     |
#    t(n)
#
# 2nd    c
#        |
#        c
#        |
#      t(n/2)
#
#
# 3rd     c     ---- c
#         |
#         c    ---- c
#         |
#         c    ---- c
#         |
#        t(n/4)

# From the above pattern, we can extrapolate that the depth of the tree is log2(n)
# For each level of the tree, we are doing c work ( or that the work takes constant time)
# c + c + c + c ..... for log2(n) times -> c * log2(n) -> O (log(n))


# Example 2: write the recurrence relation for the below and analyze the time complexity
def fun1(n):
    if n == 1:
        return
    for i in range(n):  # this for loop, perform a constant time operation for n times
        print("Hello")
    fun(n / 2)
# Solution:
# Recurrence relation: when n > 1: t(n) = t(n/2) + cn; when n == 1: O(1)
# Analysis Using Recursion Tree Method
# Base Case: When n is 1, the function returns immediately with no significant work. This is
# Iteration: For each function call, there is a loop that runs n times.
# Each iteration of this loop is a constant-time operation.
# So, the work done in each call is proportional to n, which we can denote as O(n).
# Recursive Call: The function is called recursively with the argument n / 2.

# Building the Recursion Tree
# Level 0: At the top level (level 0), the function does O(n) work.
# Level 1: On the next level, it does O(n/2) work.
# Level 2: Then O(n/4) work, and so on.
# The pattern continues, with each level doing half the work of the previous level.

# Calculating Total Work
# Level 0: O(n)
# Level 1: O(n/2)
# Level 2: O(n/4)
# Level k: O(n/2 **k) (This is the level where n/2**k = 1, meaning the base case is reached)
# Summing Across Levels
# The total work done is the sum of the work at each level.
# Total Work = O(n)+O(n/2)+O(n/4)+O(n/8)+…+O(1)
# This series is a geometric series, where each term is half of the previous term.
# The sum of such a series, converges to 2×O(n), which is O(n).

# Despite the recursive nature, the dominant factor here is the iterative work done at each level of recursion,
# which adds up to linear time complexity.
# This is an example where recursion does not significantly add to the complexity due to the decreasing size
# of the problem in each recursive call.


# Example 3: write the recurrence relation for the below and analyze the time complexity
def fun2(n):
    if n == 1:
        return
    for i in range(n):
        print("Hello")
    fun(n / 2)
    fun(n / 2)


# Example 4: Given this recurrence relation, analyze the time complexity
# t(n) = 2t(n-1) + c


# Example 5: Given this recurrence relation, analyze the time complexity
# This is hard to find the exact bound, so we need to make some assumptions
# and estimate the upper bound
# t(n) = t(n/4) + t(n/2) + cn

# Example 6: Fibonacci
def fibonacci(n):
    if n <= 0:
        print("Input a positive integer!")
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# The recurrence relation is: t(n) = t(n-1) + t(n-2)
