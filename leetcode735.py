class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk=[]
        for i in asteroids:
            while stk and stk[-1]>0 and i<0:
                if abs(stk[-1])<abs(i):
                    stk.pop()
                    continue
                elif abs(stk[-1])==abs(i):
                    stk.pop()
                    break
                else:
                    break
            else:
                stk.append(i)
        return stk