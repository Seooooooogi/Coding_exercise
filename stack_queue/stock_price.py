from collections import deque

# O(N^2)으로 문제를 풀려고 하면 효율성 통과 못함
# 스택을 활용하여 가격이 떨어지는 구간부터 안 떨어지는 곳까지 pop : O(N)
# 제한사항을 제대로 확인할 것, 또한 stack이 비는 조건을 제대로 확인할 것(버그 방지)
def solution(prices):
    answer = [0] * len(prices)
    stack = deque()
    for i, v in enumerate(prices):
        if not stack:
            stack.append((i, v))
            continue
        elif stack[-1][1] > v:
		        # 이 부분에서 while stack을 빼면 런타임 오류 발생
            while stack and stack[-1][1] > v:
                stack_i, _ = stack.pop()
                answer[stack_i] = i - stack_i
        stack.append((i, v))
        
    while stack:
        stack_i, _ = stack.pop()
        answer[stack_i] = i - stack_i
    return answer
