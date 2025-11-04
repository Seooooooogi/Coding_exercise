from collections import defaultdict

def solution(points, routes):
    answer = 0
    point_idx = defaultdict(tuple)
    paths = []
    # point_idx : 각 포인트 좌표 매핑
    for i, (r, c) in enumerate(points, 1):
        point_idx[i] = (r, c)
    # path : 이동 경로 생성, 수직 이동 먼저 하고 수평 이동
    for route in routes:
        coords = [point_idx[i] for i in route]
        path = [coords[0]]
        for (r1, c1), (r2, c2) in zip(coords, coords[1:]):
            if r1 != r2:
                dr = 1 if r2 > r1 else -1
                for r in range(r1 + dr, r2 + dr, dr):
                    path.append((r, c1))
            if c1 != c2:
                dc = 1 if c2 > c1 else -1
                for c in range(c1 + dc, c2 + dc, dc):
                    path.append((r2, c))
        paths.append(path)
    
    # counter : t 시점에서의 중복이 2 이상인 경우 충돌 판정
    T = max(len(paths[i]) for i in range(len(paths)))
    for t in range(T):
        counter = defaultdict(int)
        for path in paths:
            if t < len(path):
                counter[path[t]] += 1
        for cnt in counter.values():
            if cnt >= 2:
                answer += 1
    return answer
    
