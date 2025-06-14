class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        chars=[]
        for i in s:
            chars.append(i)
        chars=deque(chars)
        for i in range(len(chars)):
            chars.append(chars.popleft())
            if "".join(chars)==goal:
                return True
        return False

