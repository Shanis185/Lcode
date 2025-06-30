class MyStack:

    def __init__(self):
        self.q1=deque()
        self.q2=deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1,self.q2=self.q2,self.q1
        self.q2.clear()

    def pop(self) -> int:
        if self.empty():
            return None
        return self.q1.popleft()

    def top(self) -> int:
        if self.empty():
            return None
        return self.q1[0]

    def empty(self) -> bool:
            return not self.q1


