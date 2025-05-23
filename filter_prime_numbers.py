# This program is used to print all prime numbers from 1 to the given number

import math

def is_prime(n):
    if n < 2:
        return False
    if n in (2,3):
        return True
    if n%2==0 or n%3==0:
        return False
    for i in range(5,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True

def get_prime(numbers):
    return [num for num in numbers if is_prime(num)]

test_prime_numbers = list(range(1,100))
print(get_prime(test_prime_numbers))