from collections import Counter, defaultdict
from itertools import combinations

'''
- 프로그래머스 문제는 대체로 문제가 난해한 경향이 있음
- 가장 많은 빈도수를 차지면서 2번 이상 2명 이상이 주문한 품목을 코스요리로 지정
- Counter는 굳이 사용할 필요는 없을듯
- combination 사용할 때는 (iterable, 빈도수)로 사용 가능함, 뒤에 꼭 list로 다시 지정하기
- 정렬 조심
'''
def solution(orders, course):
    answer = []
    for j in course:
        frequency = defaultdict(int)
        for i in orders:
            order_combination = list(combinations(i, j))
            for k in order_combination:
		            # join 함수 기억해둘 것
		            # XW와 WX는 같기 때문에 sorted로 한번 정렬해줘야 함
                frequency["".join(sorted(k))] += 1
        # 빈 시퀀스가 있을 수 있기 때문에 if문을 달아줌
        if frequency:
		        # 참고 : max에도 key를 달아서 lambda 사용 가능
            max_frequency = max(frequency.values())
            for key, value in {k: v for k, v in frequency.items() if v != 1}.items():
                if value == max_frequency:
                    answer.append(key)
    answer.sort()
    return answer
