from collections import defaultdict

# 할인받을 수 있는 일자를 세는 것이 문제
# 문제 길이가 길고 난해하기 때문에 문제를 제대로 이해하고 제한사항을 확인
def solution(want, number, discount):
    answer = 0
    want_items = {}
    discount_items = defaultdict(int)
    for item, number in zip(want, number):
        want_items[item] = number
    for day in range(len(discount)-9):
        discount_items = defaultdict(int)
        for i in range(day, day+10):
            item = discount[i]
            if item in want_items.keys():
                discount_items[item] += 1
            if want_items == discount_items:
                answer += 1
    return answer
  
