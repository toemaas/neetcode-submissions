class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nCnt = 0
        # 1 2 3 9 9
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                nCnt += 1
                digits[i] = 0
            else:
                digits[i] += 1
                break
        
        if nCnt == len(digits):
            digits[0] = 1
            digits.append(0)

        return digits