from collections import defaultdict

def solution(genres, plays):
    answer = []
    songs = defaultdict(dict)
    famous = defaultdict(int)
    # defaultdict dict를 사용하여 이중 dict 생성
    for i in range(len(genres)):
        songs[genres[i]][i] = plays[i]
        famous[genres[i]] += plays[i]
    # key를 사용하여 item에 있는 수량을 기준으로 내림차순 정렬
    for genre, _ in sorted(famous.items(), key=lambda x: x[1], reverse=True):
        # 장르당 2번째 곡까지만 수록
        for i, (song, _) in zip(range(2), sorted(songs[genre].items(), key=lambda x: x[1], reverse=True)):
            answer.append(song)
    return answer
