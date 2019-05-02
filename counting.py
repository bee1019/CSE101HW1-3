 # Your name: Bansri Shah
# Your SBU ID: 110335850
# Your NetID: bpshah
#
# Counting Problems (Homework 1-3) starter code
# CSE 101, Fall 2018

import string

# DO NOT DELETE the following helper function!

def sieve(n): # return list of primes from 2-n
    primes = [] # all prime numbers that we find
    # create a list of (n+1) True values
    candidates = [True] * (n+1)

    for value in range(2, n + 1):
        if candidates[value] == True: # value is prime
            # Mark the multiples of value as non-prime
            for i in range(value * 2, n+1, value):
                candidates[i] = False # mark index i as composite
            primes.append(value) # record value as a prime #
    return primes


# Complete the functions that follow for this assignment

def annoyanceFactor(text):
    temp = string.ascii_lowercase + string.digits
    annoyance = 0
    currentRow = 0
    newRow = 0

    for i in range(len(text)):
        if i == 0:
            currentRow = (temp.find(text[0]) // 7)
        elif i > 0:
            newRow = (temp.find(text[i]) // 7)
            annoyance += abs(newRow - currentRow)
            currentRow = newRow
    return annoyance


def primeContainer(n):
    primes = sieve(50000)

    for p in primes:
        count = 0
        index = 0
        while primes[index] < p:
            if str(primes[index]) in str(p):
                count += 1
            if count == n:
                return p
            index += 1


# DO NOT remove the code below! You can use it to test your work.

if __name__ == "__main__":
    print('Computing annoyanceFactor("avalon31"):', annoyanceFactor("avalon31"))
    print()

    print('Computing annoyanceFactor("23fish"):', annoyanceFactor("23fish"))
    print()

    print('Computing annoyanceFactor("waterbed"):', annoyanceFactor("waterbed"))
    print()

    print('Computing annoyanceFactor("ncc1701a"):', annoyanceFactor("ncc1701a"))
    print()

    print('Computing annoyanceFactor("excelsior"):', annoyanceFactor("excelsior"))
    print()

    print('Testing primeContainer(3):', primeContainer(3))
    print()

    print('Testing primeContainer(5):', primeContainer(5))
    print()

    print('Testing primeContainer(6):', primeContainer(6))
    print()

    print('Testing primeContainer(8):', primeContainer(8))
    print()

    print()
    
