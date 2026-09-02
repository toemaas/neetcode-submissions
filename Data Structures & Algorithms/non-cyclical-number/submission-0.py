class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()

        while n != 1:
            curSum = 0
            digit = n
            while digit > 0:
                curSum += (digit % 10) ** 2
                digit //= 10
            print(curSum)
            if curSum in hashset:
                return False
            hashset.add(curSum)
            n = curSum
        return True

        