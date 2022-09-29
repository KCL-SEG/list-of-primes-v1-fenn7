"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from re import A


def primes(number_of_primes):
    list = []
    
    # represents the current number in the logic.
    cumulative = 0 
    
    while len(list) < number_of_primes:
        isPrime = True
        
        # divide the current number by all integers up to itself (excluding itself and 1).
        # if any of these do not produce a remainder, the number has more factors besides 1 and itself.
        # therefore it is not prime and will not be added to the list.
        for i in range (2, cumulative):
            if (cumulative % i) == 0:
                isPrime = False
                break
        
        if (isPrime and cumulative >= 2):
            list.append(cumulative)
            
        cumulative += 1
    
    print(list)
    return list

primes(20)