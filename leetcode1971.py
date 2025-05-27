class Solution(object):
    def validPath(self, n, edges, source, destination):
        if not edges or n==1:
            return True
        d=defaultdict(list)
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        seen=set()
        seen.add(source)
        stk=[source]
        while stk:
            node=stk.pop()
            for neigh in d[node]:
                if neigh not in seen:
                    seen.add(neigh)
                    stk.append(neigh)
                    if destination in seen:
                        return True
        return False

        