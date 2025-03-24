def solution(money):
    n = len(money)
    if n == 3:
        return max(money)
    if n == 4:
        return max(money[0] + money[2], money[1] + money[3])
    # 1: 첫번째 집을 도둑질하는 경우, 2: 두번째 집을 도둑질하는 경우
    money_1 = money[:-1]
    money_2 = money[1:]
    dp_1, dp_2 = [0] * (n-1), [0] * (n-1)
    for i in range(3):
        dp_1[i] = money_1[i]    
        dp_2[i] = money_2[i]
    dp_1[2] += dp_1[0]
    dp_2[2] += dp_2[0]
    for i in range(3, n-1):
        dp_1[i] = max(dp_1[i-2] + money_1[i], dp_1[i-3] + money_1[i])
        dp_2[i] = max(dp_2[i-2] + money_2[i], dp_2[i-3] + money_2[i])
    
    return max(max(dp_1), max(dp_2))
  
