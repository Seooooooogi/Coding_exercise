# 1. defaultdict를 사용하는 방법

from collections import defaultdict

def solution(topping):
    answer = 0
    a = defaultdict(int)
    b = defaultdict(int)
    for v in topping:
        b[v] += 1
    for i, _ in enumerate(topping):
        a[topping[i]] += 1
        b[topping[i]] -= 1
        if b[topping[i]] == 0:
            del(b[topping[i]])
        if len(a.keys()) == len(b.keys()):
            answer += 1

    return answer

# 2. Counter를 사용하는 방법

from collections import Counter

def solution(topping):
    answer = 0
    a = Counter()
    b = Counter(topping)

    for v in topping:
        a[v] += 1
        b[v] -= 1
        if b[v] == 0:
            b.pop(v)
        if len(a) == len(b):
            answer += 1

    return answer
  
