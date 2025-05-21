def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*10, reverse=True)
    return ''.join(numbers)
