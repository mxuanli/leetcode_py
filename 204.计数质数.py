class Solution:
    def countPrimes(self, n: int) -> int:
        is_num_primes = [True] * n
        count = 0
        for i in range(2, n):
            if is_num_primes[i]:
                count += 1
                # 能循环出来的都是合数
                for j in range(i * i, n, i):
                    is_num_primes[j] = False
        return count
