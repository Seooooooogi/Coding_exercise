from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 2차원 리스트를 str 일렬로 변환
        board_list = ''.join(str(num) for row in board for num in row)
        answer = '123450'
        q = deque([(board_list, board_list.index('0'), 0)])
        # board의 형태 자체를 방문 여부로 판단
        visited = set()
        # 현재 0의 위치와 바꿀 수 있는 인덱스 지정
        graph = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        # BFS
        while q:
            cur_board, zero_index, total_move = q.popleft()
            if cur_board == answer:
                return total_move
            if cur_board in visited:
                continue
            visited.add(cur_board)
            for next_move in graph[zero_index]:
                # 인덱싱을 위해 임시로 list 형태로 바꿔줌
                next_board = list(cur_board)
                next_board[zero_index], next_board[next_move] = next_board[next_move], next_board[zero_index]
                next_board = ''.join(next_board)
                q.append([next_board, next_move, total_move+1])
        return -1 
        
