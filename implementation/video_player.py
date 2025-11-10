def solution(video_len, pos, op_start, op_end, commands):
    # 모든 시간을 int 형태로 변환
    pos_int = int(pos[:2]) * 60 + int(pos[3:])
    op_start_int = int(op_start[:2]) * 60 + int(op_start[3:])
    op_end_int = int(op_end[:2]) * 60 + int(op_end[3:])
    video_len_int = int(video_len[:2]) * 60 + int(video_len[3:])
    for com in commands:
        # 오프닝 시점임을 감지
        if op_start_int <= pos_int <= op_end_int:
            pos_int = op_end_int
        if com == "next":
            # 최대 지점 보장
            if pos_int + 10 > video_len_int:
                pos_int = video_len_int
            else:
                pos_int += 10
        elif com == "prev":
            # 최소 지점 보장
            if pos_int - 10 < 0:
                pos_int = 0
            else:
                pos_int -= 10
        # 앞뒤로 오프닝 시점에 위치한지를 감지해야 함
        if op_start_int <= pos_int <= op_end_int:
            pos_int = op_end_int

    # 분과 초로 나누어서 다시 str 형태로 변환
    pos_int_min = pos_int // 60
    pos_int_sec = pos_int - pos_int_min * 60
    pos_min = "0" + str(pos_int_min) if pos_int_min < 10 else str(pos_int_min)
    pos_sec = "0" + str(pos_int_sec) if pos_int_sec < 10 else str(pos_int_sec)
    answer = pos_min + ":" + pos_sec
    return answer
    
