def solution(enroll, referral, seller, amount):
    answer = []
    employ_dict = {}
    profit_dict = {}
    for i, j in zip(enroll, referral):
        employ_dict[i] = j
        profit_dict[i] = 0
    for k, l in zip(seller, amount):
        profit = l * 100
        current_employ = k
        # 돈이 0원이면 더 이상 계산할 필요가 없음 -> 효율성
        while profit > 0:
            # 단, 10% 를 계산할 때에는 원 단위에서 절사하며, 10%를 계산한 금액이 1 원 미만인 경우에는 
            # 이득을 분배하지 않고 자신이 모두 가진다. -> round 대신 // 10 사용해야 함
            my_profit = profit - profit // 10
            profit = profit // 10
            profit_dict[current_employ] += my_profit
            if employ_dict[current_employ] == "-":
                break
            current_employ = employ_dict[current_employ]
            
    return list(profit_dict.values())
