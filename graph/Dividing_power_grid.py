from collections import defaultdict

def solution(n, wires):
    answer = 100
    
    def dfs(node):
        nonlocal amount
        if node in visited:
            return
        visited.add(node)
        amount += 1
        for next_node in graph[node]:
            dfs(next_node)
    
    for i in range(len(wires)):
        visited = set()
        amount = 0
        graph = defaultdict(list)
        for j in range(len(wires)):
            if i == j:
                continue        
            graph[wires[j][0]].append(wires[j][1])
            graph[wires[j][1]].append(wires[j][0])
        
        dfs(next(iter(graph)))
        answer = min(answer, abs(2 * amount - n))
    return answer
