class Solution:
    def concatenatedBinary(self, n: int) -> int:
        answer = 0
        for i in range(1, n+1):
		        # 현재 숫자의 크기만큼 2비트 자리수 공간을 만들어 준 뒤 or 연산으로 현재 숫자를 이어붙임
		        # modular를 바로 연산해서 오버헤드를 줄임
            answer = (answer << i.bit_length() | i) % (10**9 + 7)
            
        return answer
        
