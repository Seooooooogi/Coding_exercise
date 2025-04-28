from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # 원형을 직접 구현하는 대신 weak의 길이를 두배로 늘려줌
    # 두배로 늘려도 괜찮은 이유 -> (i, i+length)만큼만 검사하면 됨
    for i in range(length):
        weak.append(weak[i]+n)
    
    # 최대 결과 + 1로 answer 초기화
    answer = len(dist) + 1
    
    for i in range(length):
        # 순열 사용(순열 내 list 등 배치, 몇개 뽑을건지 순)
        for comp in permutations(dist, len(dist)):
            cnt = 1
            # 초기 배치
            position = weak[i] + comp[cnt-1]
            # 추가 배치를 통해 부족하면 한명씩 더 투입
            for j in range(i, i+length):
                if position < weak[j]:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    position = weak[j] + comp[cnt-1]
            answer = min(answer, cnt)
    return answer if answer <= len(dist) else -1
