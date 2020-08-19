# https://leetcode.com/problems/plus-one/

def plusOne(digits):
    return list(str(int("".join("{0}".format(n) for n in digits)) + 1))

print(plusOne([9,9,9,9,9]))