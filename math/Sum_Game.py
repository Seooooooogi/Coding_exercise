class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2
        left_sum = sum(int(n) for n in num[:half] if n.isdigit())
        right_sum = sum(int(n) for n in num[half:] if n.isdigit())
        left_count = num[:half].count('?')
        right_count = num[half:].count('?')

        # Alice는 count의 차이만큼 +-9만큼의 이득을 볼 수 있음
        # 턴이 하나씩 진행되기 때문에 alice의 추가 기대 이득은 ((left_count - right_count) * 9) / 2
        # 따라서 그 기대 이득만큼의 차이가 좌우의 합 차이인지 확인해서 다르다면 alice win, 같다면 bob win
        return (left_sum - right_sum) * 2 != 9 * (right_count - left_count)
        
