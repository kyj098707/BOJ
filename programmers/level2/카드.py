from math import gcd
from functools import reduce

def check(arrayA, arrayB):
    gcd_A = reduce(gcd, arrayA, arrayA[0])
    factors = [i for i in range(1, gcd_A//2+1) if not gcd_A % i]
    factors.append(gcd_A)
    for factor in factors[::-1]:
        if all(i % factor for i in arrayB):
            return gcd_A
    return 0

def solution(arrayA, arrayB):
    return max(check(arrayA, arrayB), check(arrayB, arrayA))

arrayA = [1,2,3,4,5,6,7,8,9,10]
sum_A = reduce(lambda x,y:x+y,arrayA)

print(sum_A)