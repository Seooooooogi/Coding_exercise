class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split("-")
        answer = 0
        month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year = int(year)
        # 윤년의 규칙 : 4년마다 돌아옴. 100년은 평년. 하지만 400으로 나눌 수 있으면 윤년
        chk_leap_year = True if (year % 4 == 0) and (year % 100 != 0) else False
        if year == 2000:
            chk_leap_year = True
        for i in range(int(month)-1):
            if i == 1 and chk_leap_year:
                answer += month_day[i] + 1
            else:
                answer += month_day[i]
        answer += int(day)
        return answer
        
