class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        minTemp = float("inf")
        stack = []
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            minTemp = min(minTemp, temp)
            if temp > minTemp:
                while stack and temp > stack[-1][0]:
                    index = stack.pop()[1]
                    res[index] = idx - index
                minTemp = temp
            stack.append([temp, idx])
        return res