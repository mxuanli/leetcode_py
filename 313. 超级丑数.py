class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n == 1:
            return 1
        set_num = {1}  # 保证不重复
        list_num = [1]  # 1是第一个
        for i in range(n):
            num = heapq.heappop(list_num)
            for p in primes:
                next_num = num * p  # primes内的数字相乘质因数一定都在primes内
                if next_num not in set_num:
                    set_num.add(next_num)
                    heapq.heappush(list_num, next_num)
        return num
