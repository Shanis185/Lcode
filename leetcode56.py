class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []
        result=[]
        intervals.sort(key=lambda x:x[0])
        result=[intervals[0]]
        
        for i in range(1,len(intervals)):
            last=result[-1]
            current=intervals[i]

            if last[1]>=current[0]:
                last[1]=max(last[1],current[1])
            else:
                result.append(current)
        return result

-----------------------------------------------------------------
class Solution(object):
    def merge(self, intervals):
        
        result=[]
        intervals.sort(key=lambda x:x[0])
        for interval in intervals:
            if not result or result[-1][1]<interval[0]:
                result.append(interval)
            else:
                result[-1][1]=max(result[-1][1],interval[1])
        return result