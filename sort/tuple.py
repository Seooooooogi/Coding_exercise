def solution(s):
    answer = []
    # split 조건을 여러 개 사용하고 싶을 경우
    # re.split(r'(조건)', s)를 사용해야 함 -> 어느 하나라도 있으면 분리
    # 하지만 re는 공백 제거는 불가능
    new_s = s[2:-2].split("},{")
    new_s.sort(key=lambda x:len(x))
    for i in new_s:
        j = i.split(",")
        for k in j:
            if int(k) not in answer:
                answer.append(int(k))
    return answer
