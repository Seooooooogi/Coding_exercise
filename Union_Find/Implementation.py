def find(x, parents):
    # 현재 노드와 부모 노드가 동일하지 않을 경우 계속 부모 노드를 거슬러 올라감
    if parents[x] != x:
        parents[x] = find(parents[x], parents)
    return parents[x]

def union_set(x, y, parents, rank_data):
    root1 = find(x, parents)
    root2 = find(y, parents)

    
    if root1 != root2:
        # 랭크가 큰 쪽으로 작은 쪽이 합쳐지는 형태로 연산
        if rank_data[root1] < rank_data[root2]:
            parents[root1] = root2
        elif rank_data[root1] > rank_data[root2]:
            parents[root2] = root1
        # 두 랭크가 동일한 경우 그냥 root1에 맞추고 root1의 랭크를 1 늘려줌
        else:
            parents[root2] = root1
            rank_data[root1] += 1

def solution(k, operations):
    parents = list(range(k))
    rank_data = [0] * k
    results = []

    for op in operations:
        if op[0] == "u":
            x = int(op[1])
            y = int(op[2])
            union_set(x, y, parents, rank_data)
        elif op[0] == "f":
            x = int(op[1])
            y = int(op[2])
            results.append(find(x, parents) == find(y, parents))

    return results
  
