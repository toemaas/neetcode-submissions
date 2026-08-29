class MinStack:

    def __init__(self):
        self.m = []
        self.arr = []

    def push(self, val: int) -> None:
        if len(self.m) < 1:
            self.m.append(val)
            self.arr.append(val)
            return
        if val < self.m[-1]:
            self.m.append(val)
        else:
            self.m.append(self.m[-1])
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()
        self.m.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.m[-1]
