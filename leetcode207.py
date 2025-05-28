class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        d=defaultdict(list)
        for u,v in prerequisites:
            d[u].append(v)
        visited=2
        unvisited=0
        visiting=1
        states=[0]*numCourses
        def dfs(node):
            state=states[node]
            if state==visited:
                return True
            if state==visiting:
                return False
            states[node]=visiting

            for neigh in d[node]:
                if not dfs(neigh):
                    return False
            states[node]=visited
            return True

            
        




        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True
        