def solution(diffs, times, limit):
    n = len(times)
    def is_possible(level):
        cul_time = times[0]
        for i in range(1, n):
            if diffs[i] <= level:
                cul_time += times[i]
            else:
                cul_time += (diffs[i] - level) * (times[i-1] + times[i]) + times[i]
            if cul_time > limit:
                return False
        return True
    
    left, right = 1, max(diffs)
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
          
    return answer
    
