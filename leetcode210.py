class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        d=defaultdict(list)
        for u,v in prerequisites:
            d[v].append(u)
        visited=2
        unvisited=0
        visiting=1
        states=[0]*numCourses
        res=[]
        
        if numCourses==1:
            return [0]
        def dfs(node):
            state=states[node]
            if state==2:
                
                return True
            if state==1:
                return False
            states[node]=1

            for neigh in d[node]:
                if not dfs(neigh):
                    return False
            states[node]=2
            res.append(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return []
            
                
        return res[::-1]
        
