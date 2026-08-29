class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2, 3, 3, 5, 5 target = 6
        n = len(numbers)
        l, r = 0, n - 1
        while l < r:
            total = numbers[l] + numbers[r]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return [l + 1, r + 1]