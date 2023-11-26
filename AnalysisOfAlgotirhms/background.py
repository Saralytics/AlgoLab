# Write a simple function which does sum of n natural number
# input: n = 3
# output: 6 //1+2+3
# There are a few ways to do this

def sum_int_0(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


def sum_int_1(n):
    result = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            result += 1
    return result


def sum_int_3(n):
    return n * (n + 1) / 2


# Asymptotic analysis: theoretic
# Could do this analysis by pseudocode even. Concerned with order of growth

# sum_int_0:  -> c1 (constant)
# sum_int_1:  -> c2*n + c3
# sum_int_2:  -> c4 * n*n + c5 * n + c6
