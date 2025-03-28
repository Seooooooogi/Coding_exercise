def solution(record):
    answer, orders = [], []
    user = {}
    for i in record:
        i = i.split(" ")
        order, uid = i[0], i[1]
        if order == "Enter":
            nickname = i[2]
            user[uid] = nickname
            orders.append((order, uid))
        elif order == "Change":
            nickname = i[2]
            user[uid] = nickname
        else:
            orders.append((order, uid))
    
    for i in orders:
        if i[0] == "Enter":
            answer.append(f"{user[i[1]]}님이 들어왔습니다.")
        else:
            answer.append(f"{user[i[1]]}님이 나갔습니다.")
    return answer
