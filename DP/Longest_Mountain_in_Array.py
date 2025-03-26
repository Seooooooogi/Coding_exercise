class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        up = [0] * n
        down = [0] * n
        # 좌측부터 올라가는 언덕을 셈
        for i in range(1, n):
            if arr[i-1] < arr[i]:
                up[i] = up[i-1] + 1
        # 우측부터 올라가는 언덕을 셈(= 좌측 입장에서는 내려가는 언덕임)
        for i in range(n-2, 0, -1):
            if arr[i] > arr[i+1]:
                down[i] = down[i+1] + 1
        
        # UP과 DOWN이 만나는 지점은 산꼭대기이므로 거기에서 1을 더한 값을 정답으로 만듬
        # 주의사항 : 빈 array가 나올 수 있으므로(mountain이 없는 경우) or를 사용하면 max에서 empty sequence에 대한 오류 예외처리 가능함
        return max([u+d+1 for u, d in zip(up, down) if u and d] or [0])
