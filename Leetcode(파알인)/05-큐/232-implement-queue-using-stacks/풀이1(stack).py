class MyQueue:
    def __init__(self):
        self.input=[]
        self.output=[]

    def push(self, x: int) -> None:
        if self.output:
            for _ in range(len(self.output)):
                self.input.append(self.output.pop())
        
        self.input.append(x)
    
        for _ in range(len(self.input)):
            self.output.append(self.input.pop())
            

    def pop(self) -> int:
        return self.output.pop()
        

    def peek(self) -> int:
        return self.output[-1]

    def empty(self) -> bool:
        return len(self.output)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()