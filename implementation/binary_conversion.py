def solution(s):
    zero_count = 0
    binary_count = 0
    while s != "1":
        new_s = ""
        for i in s:
            if i == "0":
                zero_count += 1
            else:
                new_s += "1"
        s = str(bin(len(new_s)))[2:]
        binary_count += 1
    return [binary_count, zero_count]
    
