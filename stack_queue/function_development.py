import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    # deque으로 큐 관리
    q = deque()
    for i, v in zip(progresses, speeds):
        q.append((i, v))
    total = 0
    while q:
        progress, speed = q.popleft()
        if total == 0:
            estimated_days = math.ceil((100 - progress) / speed)
            total += 1
            continue
        if progress + speed * estimated_days >= 100:
            total += 1
            continue
        else:
            answer.append(total)
            total = 0
            q.appendleft((progress, speed))
    
    # 마지막으로 남은 일자들을 더해줘야 함
    answer.append(total)
    return answer
