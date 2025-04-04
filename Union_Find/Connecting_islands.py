def solution(n, costs):

    # union-find 구현
    def find(x, parents):
        if parents[x] != x:
            parents[x] = find(parents[x], parents)
        return parents[x]

    # implementation과 차이점은 x == y 조건을 밖에다 함
    def union(x, y, rank_data, parents):
        root1 = find(x, parents)
        root2 = find(y, parents)
        
        if rank_data[root1] < rank_data[root2]:
            parents[root1] = root2
        elif rank_data[root1] > rank_data[root2]:
            parents[root2] = root1
        else:
            parents[root2] = root1
            rank_data[root1] += 1

    # 최소 가격부터 참조해서 섬을 연결
    costs.sort(key=lambda x: x[2])
    parents = [i for i in range(n)]
    rank_data = [0] * n
    edge_amount = 0
    answer = 0
    
    for x, y, cost in costs:
        # 모든 섬이 연결되는 최소 조건은 n - 1일 떄
        if edge_amount == (n - 1):
            break
        
        x = find(x, parents)
        y = find(y, parents)

        # 순환이 만들어지는 조건은 두 노드의 부모가 같을 때 연결하는 것이므로 배제
        if x != y:
            union(x, y, rank_data, parents)
            answer += cost
            edge_amount += 1
        
    return answer
