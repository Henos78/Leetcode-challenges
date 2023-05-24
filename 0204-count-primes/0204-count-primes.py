class Solution:
    def countPrimes(self, n: int) -> int:
        
    # using Sieve of Eratosthenes Algorithm to find  prime numbers to a given limit
        if n <= 2:
            return 0

        # Initialize a boolean array to track prime numbers
        is_prime = [True] * n

        # 0 and 1 are not prime, so set their values to False
        is_prime[0] = is_prime[1] = False

        # Use the Sieve of Eratosthenes to mark non-prime numbers
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False

        # Count the number of prime numbers
        count = sum(is_prime)
        return count
