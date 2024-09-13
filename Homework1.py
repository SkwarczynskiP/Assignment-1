# Question 1:
# Implement the Euclidean Algorithm and use it to solve this problem
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
class Solution1:
    def findGCD(self, nums: List[int]) -> int:
        maxNum, minNum = abs(max(nums)), abs(min(nums))

        while minNum > 0:
            r = maxNum % minNum
            maxNum, minNum = minNum, r

        return maxNum


# Question 2:
# Implement the Sieve of Eratosthenes and use it to solve this problem
# https://leetcode.com/problems/count-primes/description/

class Solution2:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        prime = [True] * n
        prime[0], prime[1] = False, False

        for p in range(2, int(n**0.5) + 1):
            if prime[p]:
                for i in range(p * p, n, p):
                    prime[i] = False

        return sum(prime)