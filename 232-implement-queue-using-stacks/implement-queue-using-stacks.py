from collections import deque
class MyQueue:

    def __init__(self):
        self.re=deque()
        
    def push(self, x: int) -> None:
        self.re.append(x)    

    def pop(self) -> int:
        return self.re.popleft() if re else None

    def peek(self) -> int:
        return self.re[0] if re else None
        
    def empty(self) -> bool:
        return len(self.re)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()