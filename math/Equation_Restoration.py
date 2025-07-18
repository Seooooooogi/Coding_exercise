# 현재 연산에서 큰 자릿수를 찾음
def max_digit_in_string(s):
    return max(int(ch) for ch in s)

# 현재 예측하는 진수에서 유효한 연산(진수보다 더 큰 자릿수가 있는지)인지 확인
def is_valid_base_for_expression(a, b, c, base):
    for val in [a, b, c]:
        if any(int(ch) >= base for ch in val):
            return False
    return True

# 현재 예측하는 진수에서 유효한 연산인지 확인
def is_valid_expression(a, b, c, op, base):
    try:
        a_val = int(a, base)
        b_val = int(b, base)
        c_val = int(c, base)
    except ValueError:
        return False
    if op == '+':
        return a_val + b_val == c_val
    else:
        return a_val - b_val == c_val

# 자릿수(base)에 따른 실제 연산 수행
def evaluate_expression(a, b, op, base):
    a_val = int(a, base)
    b_val = int(b, base)
    res = a_val + b_val if op == '+' else a_val - b_val
    digits = []
    if res == 0:
        return '0'
    while res > 0:
        digits.append(str(res % base))
        res //= base
    return ''.join(reversed(digits))

def solution(expressions):
    known = []
    unknown = []

    for exp in expressions:
        A, op, B, _, C = exp.split()
        if C == 'X':
            unknown.append((A, op, B))
        else:
            known.append((A, op, B, C))

    valid_bases = []
    # 2~9진수를 순회하면서 실제로 가능한 진수만 valid_bases에 추가
    for base in range(2, 10):
        ok = True
        for A, op, B, C in known:
            if not is_valid_base_for_expression(A, B, C, base):
                ok = False
                break
            if not is_valid_expression(A, B, C, op, base):
                ok = False
                break
        for A, op, B in unknown:
            if not is_valid_base_for_expression(A, B, "0", base):
                ok = False
                break
        if ok:
            valid_bases.append(base)

    result = []
    for exp in expressions:
        A, op, B, _, C = exp.split()
        if C != 'X':
            continue
        else:
            candidates = set()
            for base in valid_bases:
                try:
                    res = evaluate_expression(A, B, op, base)
                    candidates.add(res)
                except:
                    continue
            # 가능한 경우의 수가 하나면 answer에 해당 답을 추가
            if len(candidates) == 1:
                filled = candidates.pop()
                result.append(f"{A} {op} {B} = {filled}")
            # 아니라면 답은 ?임
            else:
                result.append(f"{A} {op} {B} = ?")
    return result
