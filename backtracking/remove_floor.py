def solution(board, aloc, bloc):
    answer = -1
    m, n = len(board), len(board[0])
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    def back(a_pos, b_pos, visited, step):
        y, x = a_pos if step % 2 == 0 else b_pos
        win_steps, lose_steps = [], []
        can_move = False
        b_win = True
        
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < m and 0 <= nx < n and (ny, nx) not in visited and board[ny][nx]:
                can_move = True
                if a_pos == b_pos:
                    return True, step + 1
                
                # visited.add((y, x))
                # 여기서 add를 하면 뒤의 코드에 영향을 끼치기 때문에 안에서 union 연산을 해줘야 함
                if step % 2 == 0:
                    win, total_steps = back([ny, nx], b_pos, visited | {(y, x)}, step+1)
                else:
                    win, total_steps = back(a_pos, [ny, nx], visited | {(y, x)}, step+1)
                b_win &= win
                if win:
                    win_steps.append(total_steps)
                else:
                    lose_steps.append(total_steps)

        if not can_move:
            return False, step
        if b_win:
            return False, max(win_steps)
                
        return True, min(lose_steps)
    
    _, steps = back(aloc, bloc, set(), 0)
    return steps
  
