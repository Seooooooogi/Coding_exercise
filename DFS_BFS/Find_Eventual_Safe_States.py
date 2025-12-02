class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = {}
        ans = []
        def dfs(i):
            # 이미 safe 노드인지 판별된 노드는 더 이상 판별하지 않음
            if i in safe:
                return safe[i]
            
            # 우선 safe 노드를 false라 가정
            safe[i] = False
            # 이 노드의 연결 관계를 살펴보면서 해당 노드가 safe 노드인지 판별
            # 일부 노드는 terminal node기 때문에 for 문을 거치지 않고 바로 true로 판별
            # 연결중인 노드 중 하나라도 safe 노드가 아니라면 false를 유지
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[i]
            # 아니라면 이 노드는 safe 노드 확정
            safe[i] = True
            return safe[i]
        
        for i in range(n):
            if dfs(i):
                ans.append(i)
        
        return ans
