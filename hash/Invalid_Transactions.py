from collections import defaultdict
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        answer = []
        dic = {}
        for trans in transactions:
            name, time, _, city = trans.split(",")
            if name not in dic:
                dic[name] = defaultdict(list)
            dic[name][city].append(time)
            
        for trans in transactions:
            name, std_time, std_amount, std_city = trans.split(",")
            # chk : 한 번이라도 적발됐으면 answer에 추가하고 더 볼 필요가 없으므로 flag 생성
            chk = False
            # 조건 1. 승인금액 1000 이상
            if int(std_amount) > 1000:
               answer.append(trans)
               continue
            # 조건 2. 다른 도시에 60분 이내 거래
            for city, val in dic[name].items():
                if std_city != city:
                    for time in val:
                        if abs(int(std_time) - int(time)) <= 60:
                            answer.append(trans)
                            chk = True
                            break
                    if chk is True:
                        break
        return answer

