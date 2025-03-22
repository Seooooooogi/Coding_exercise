class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        # board에서 list 형태로 미리 만들어서 assignment를 가능하게 하고 후에 join으로 해결
        board = [["."] * n for _ in range(n)]
        # set으로 위반 여부 확인
        cols = set()
        diag1 = set()
        diag2 = set()
        def getAns(row):
            if row == n:
		            # join을 통해서 문제가 원하는 str 형태로 다시 저장
                copy = ["".join(r) for r in board]
                answer.append(copy)
                return
            else:
                for col in range(n):
		                # 알아두면 좋은 점 : 대각선은 우하향쪽으로는 row - col이 같고, 좌상향쪽으로는 row + col이 같다!
                    if col in cols or (row-col) in diag1 or (row+col) in diag2:
                        continue
                    board[row][col] = "Q"
                    cols.add(col)
                    diag1.add(row-col)
                    diag2.add(row+col)
										# 백트래킹
                    getAns(row+1)

                    board[row][col] = "."
                    cols.remove(col)
                    diag1.remove(row-col)
                    diag2.remove(row+col)
        
        getAns(0)
        return answer
            
