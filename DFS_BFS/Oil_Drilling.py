from collections import deque

def solution(land):
    m, n = len(land), len(land[0])
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    group = [[0] * n for _ in range(m)]
    group_size = {}
    
    answer = 0
    group_num = 1
    for i in range(m):
        for j in range(n):
            if land[i][j] == 1 and group[i][j] == 0:
                group[i][j] = group_num
                size = 0
                q = deque([(i, j)])
                while q:
                    r, c = q.popleft()    
                    size += 1
                    for k in range(4):
                        nr, nc = r + dr[k], c + dc[k]
                        if 0 <= nr < m and 0 <= nc < n and land[nr][nc] == 1 and group[nr][nc] == 0:
                            group[nr][nc] = group_num
                            q.append((nr, nc))
                
                group_size[group_num] = size
                group_num += 1
    
    for i in range(n):
        best = 0
        seen_group = set()
        for j in range(m):
            if group[j][i] != 0:
                seen_group.add(group[j][i])
        for g in seen_group:
            best += group_size[g]
        answer = max(answer, best)
        
    return answer
  
