class MinStack:

    def __init__(self):
        self.minimum = None
        self.stack = []

    def push(self, val: int) -> None:
        #first check and update minimum
        if self.minimum == None or self.minimum > val:
            self.minimum = val
        #update stack
        self.stack.append(val)

    def pop(self) -> None:
        if self.minimum == self.stack.pop():
            if len(self.stack) > 0:
                self.minimum = min(self.stack)
            else:
                self.minimum = None
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()