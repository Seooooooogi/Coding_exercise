from collections import deque, defaultdict

def solution(info, edges):
    answer = 0
    info_dict = {}
    edge_dict = defaultdict(list)
    for i, v in enumerate(info):
        info_dict[i] = v
    for i, j in edges:
        edge_dict[i].append(j)
    q = deque()
    q.append((0, 1, 0, set()))
    while q:
        node, sheep, wolf, visited = q.popleft()
        answer = max(sheep, answer)
        # 일반적인 다시 방문하지 않을 visited가 아니라 현재까지 방문한 노드 중에서 추가로 방문할 수 있는 노드를 확인함
        visited.update(edge_dict[node])
          
        for next_node in visited:
            # 늑대일 경우 양의 수를 고려해서 append
            if info_dict[next_node] == 1:
                if sheep != wolf + 1:
                    # 현재 위치한 노드의 자식 노드를 다시 방문하도록 하지 않기 위해 visited에서 next node를 빼줌
                    q.append((next_node, sheep, wolf + 1, visited - {next_node}))
            # 아닐 경우 무조건 append
            else:
                q.append((next_node, sheep + 1, wolf, visited - {next_node}))
    return answer
    
