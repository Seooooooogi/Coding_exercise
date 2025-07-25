def solution(scores):
    n = len(scores)
    wanho_score = scores[0]
    wanho_sum = sum(wanho_score)
    
    # 1. 완호가 인센티브를 받지 못하는 경우
    for i in range(n):
        if wanho_score[0] < scores[i][0] and wanho_score[1] < scores[i][1]:
            return -1
    
    arr = [(x, y, x + y) for x, y in scores]
    arr.sort(key=lambda x:x[0], reverse=True)
    
    max_y = -1
    answer = 0
    i = 0

    while i < n:
        # 같은 근무 태도 점수를 가진 사람들을 그룹으로 나눔
        x_curr = arr[i][0]
        j = i
        while j < n and arr[j][0] == x_curr:
            j += 1
        
        # 첫 번째 그룹은 인센티브 받지 못하는 사람이 없으므로 max_y = -1
        # 두 번째 그룹부터 max_y보다 작으면 인센티브를 받지 못함
        # 완호보다 점수 높은 사람만큼 등수를 올림
        for k in range(i, j):
            y_k, sum_k = arr[k][1], arr[k][2]
            if y_k >= max_y and sum_k > wanho_sum:
                answer += 1
        
        # 다음 그룹에 참고로 활용할 현재 그룹의 max_y 갱신
        for k in range(i, j):
            if arr[k][1] > max_y:
                max_y = arr[k][1]

        i = j
    
    # 원호보다 등수 높은 사람을 전부 계산했기 때문에 +1이 정답
    return answer + 1
