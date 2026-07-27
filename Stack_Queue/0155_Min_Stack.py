"""
Problem: 155. Min Stack
Difficulty: Medium
"""

class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, value: int) -> None:
        self.s1.append(value)
        if len(self.s2) == 0 or (value <= self.s2[-1]):
            self.s2.append(value)

    def pop(self) -> None:
        if self.s2[-1] == self.s1[-1]:
            self.s2.pop()
        self.s1.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.s2[-1]


#maintaining the two stacks and make sure when to dlete elemnts from both of them and also what to return for min and main stack

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
