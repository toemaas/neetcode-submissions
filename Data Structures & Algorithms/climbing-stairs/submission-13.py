class Solution:
    def climbStairs(self, n: int) -> int:
        climb1, climb2 = 1, 1
        # 2
        # 1: 1 way to reach 2
        # 0: 
        for i in range(n - 1):
            temp = climb1
            climb1 = climb1 + climb2
            climb2 = temp
        
        return climb1