class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos = list(zip(position, speed))
        pos.sort(reverse=True)
        for car in pos:
            time = (target - car[0]) / car[1]
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        
        return len(stack)