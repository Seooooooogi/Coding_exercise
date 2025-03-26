def solution(board):
    answer = 0
    m, n = len(board), len(board[0])
    for i in range(1, m):
        for j in range(1, n):
            # 정사각형을 구할 수 있는 최소 단위의 박스를 고른 뒤
            if board[i][j] == 1:
                # 좌상단 대각선, 위, 왼쪽이 모두 1일 때 2가 되도록 DP를 설정
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
    
    # 전체 board에서 최댓값을 구함
    return max(max(row) for row in board) ** 2
    
