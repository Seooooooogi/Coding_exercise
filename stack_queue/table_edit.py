def solution(n, k, cmd):
    answer = ["O"] * n
    delete_history = []
    # 가상의 인덱스를 도입해 행 번호로 관리
    # 가장 윗 행과 가장 마지막 행의 연산을 위하여 2칸 더 생성
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 2)]
    
    # 실제 인덱스에 맞추기 위해 +1을 더해줌
    k += 1
    
    for i in cmd:
        # 삭제 연산
        # 윗 행의 down은 현재 아래 행이 됨
        # 아래 행의 up은 현재 윗 행이 됨
        # 커서는 맨 아래 커서가 아니면 내리고 그렇지 않다면 올림
        if i.startswith("C"):
            delete_history.append(k)
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            k = up[k] if n < down[k] else down[k]
        # 복구 연산
        # 커서 k 대신 복구해야 할 행 번호를 가져와서 원래대로 돌림
        elif i.startswith("Z"):
            restore = delete_history.pop()
            up[down[restore]] = restore
            down[up[restore]] = restore
        else:
            # UP 혹은 DOWN 연산
            # 행 번호가 달라졌을 수 있으므로 up과 down 리스트에서 찾아야 함
            command, amount = i.split()
            if command == "U":
                for _ in range(int(amount)):
                    k = up[k]
            else:
                for _ in range(int(amount)):
                    k = down[k]
    
    # 전부 맞다고 가정하고 delete history에 있는 행 번호를 맞추고 X 표기
    for d in delete_history:
        answer[d - 1] = "X"
        
    return ''.join(answer)
  
