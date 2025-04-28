# 1. 최초 풀이
from itertools import combinations_with_replacement

def solution(n, info):
    def calculate_score(info1, info2):
        score1, score2 = 0, 0
        for i in range(10):
            if info1[i] == 0 and info2[i] == 0:
                continue
            elif info1[i] < info2[i]:
                score2 += (10 - i)
            else:
                score1 += (10 - i)
        return score1, score2
    
    max_score = 0
    max_comb = [0] * 11
    # 중복을 허용하는 조합 -> combinations_with_replacement
    for scores in list(combinations_with_replacement(range(11), n)):
        info2 = [0] * 11
        for i in scores:
            info2[i] += 1
        score1, score2 = calculate_score(info, info2)
        if score2 > score1:
            if (score2 - score1) > max_score:
                max_score = score2 - score1
                max_comb = info2
            elif (score2 - score1) == max_score:
		            # 더 낮은 점수를 많이 맞춘 쪽으로 갱신해야 하는데... 더 좋은 코드가 없나?
                for j in range(10, 0, -1):
                    if info2[j] > max_comb[j]:
                        max_comb = info2
                        break
                    if info2[j] < max_comb[j]:
                        break

    return max_comb if max_score > 0 else [-1]

# 2. 더 정교한 풀이
from itertools import combinations_with_replacement
from collections import Counter

def solution(n, info):
    def calculate_score(info1, combi):
        score1, score2 = 0, 0
        for i in range(1, 11):
            if info1[10-i] < combi.count(i):
                score2 += i
            elif info1[10-i] > 0:
                score1 += i
        return score1, score2
    
    def calculate_best_comb(n, info):
        max_diff = 0
        max_comb = {}
        for combi in list(combinations_with_replacement(range(11), n)):
            cnt = Counter(combi)
            score1, score2 = calculate_score(info, combi)
            diff = score2 - score1
            if diff > max_diff:
                max_diff = diff
                max_comb = cnt
                
        return max_diff, max_comb
    
    max_diff, max_comb = calculate_best_comb(n, info)
    if max_diff > 0:
        answer = [0] * 11
        for score in max_comb:
            answer[10 - score] = max_comb[score]
        return answer
    else:
        return [-1]
