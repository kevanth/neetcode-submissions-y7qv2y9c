class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        i = 0

        while i < len(self.minstack):
            if self.minstack[i] < val:
                break
            i += 1
        
        self.minstack = self.minstack[0:i] + [val] + self.minstack[i:]
        print(self.minstack)

    def pop(self) -> None:
        #need a min stack so popping will give next min
        val = self.stack.pop()
        self.minstack.remove(val)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]