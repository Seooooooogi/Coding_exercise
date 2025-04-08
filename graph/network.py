from collections import defaultdict

def solution(n, computers):
    answer = 0
    visited = set()
    graph = defaultdict(list)
    # 네트워크 그래프 생성
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                graph[i].append(j)
    
    def dfs(node):
        visited.add(node)
        for next_node in graph[node]:
            if next_node not in visited:
                dfs(next_node)

    # 순회하면서 아직 방문하지 않았단 것은 네트워크를 새로 생성할 수 있는 것
    for i in range(n):
        if i not in visited:
            answer += 1
            dfs(i)
            
    return answer
