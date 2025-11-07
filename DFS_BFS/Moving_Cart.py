def solution(maze):
    m, n = len(maze), len(maze[0])
    dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
    red_visited, blue_visited = set(), set()
    answer = 0
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_end = (i, j)
            elif maze[i][j] == 4:
                blue_end = (i, j)
    
    # check_valid_pos : 말이 벽에 가거나 범위를 벗어나거나 방문한 데를 다시 방문했는지 확인
    def check_valid_pos(pos_r, pos_c, visited):
        if pos_r < 0 or pos_r >= m or pos_c < 0 or pos_c >= n or (pos_r, pos_c) in visited or maze[pos_r][pos_c] == 5:
            return True
        return False
    
    # check_swap_or_duplicate : 두 말이 서로 겹치거나 스왑했는지 확인
    def check_swap_or_duplicate(pos_r, pos_c, prev_r, prev_c):
        if pos_r == prev_r and pos_c == prev_c:
            return True
        return False
        
    def back(cur_red, cur_blue, turn):
        nonlocal answer
        # 조기종료 : 최소 턴을 구해야 함
        if turn >= answer and answer != 0:
            return
        if cur_red == red_end and cur_blue == blue_end:
            answer = turn
            return
        # 빨간 말과 파란 말은 독립적으로 한 턴에 한 번 움직일 수 있으므로 이중 for 문 사용
        for i in range(4):
            for j in range(4):
                # 말이 목적지에 도착하면 더 이상 움직이지 않음
                if cur_red != red_end:
                    red_nr, red_nc = cur_red[0] + dr[i], cur_red[1] + dc[i]
                    if check_valid_pos(red_nr, red_nc, red_visited):
                        continue
                else:
                    red_nr, red_nc = cur_red[0], cur_red[1]
                if cur_blue != blue_end:
                    blue_nr, blue_nc = cur_blue[0] + dr[j], cur_blue[1] + dc[j]
                    if check_valid_pos(blue_nr, blue_nc, blue_visited):
                        continue
                else:
                    blue_nr, blue_nc = cur_blue[0], cur_blue[1]    
                    
                if check_swap_or_duplicate(red_nr, red_nc, blue_nr, blue_nc):
                    continue
                if check_swap_or_duplicate(red_nr, red_nc, cur_blue[0], cur_blue[1]) and check_swap_or_duplicate(blue_nr, blue_nc, cur_red[0], cur_red[1]):
                    continue
                
                red_visited.add((red_nr, red_nc))
                blue_visited.add((blue_nr, blue_nc))
                back((red_nr, red_nc), (blue_nr, blue_nc), turn+1)
                # 말이 이미 목적지에 도착한 경우라면 keyerror가 발생할 수 있음
                if cur_red != red_end:
                    red_visited.remove((red_nr, red_nc))
                if cur_blue != blue_end:
                    blue_visited.remove((blue_nr, blue_nc))
        return
    
    red_visited.add(red_start)
    blue_visited.add(blue_start)
    turn = back(red_start, blue_start, 0)
    return answer
