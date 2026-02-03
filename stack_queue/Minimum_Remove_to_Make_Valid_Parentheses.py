from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        q = deque()
        s_list = list(s)
        for i, v in enumerate(s):
            if v == "(":
                q.append(i)
            elif v == ")":
                if q:
                    q.pop()
                else:
                    s_list[i] = ""
        
        while q:
            s_list[q.pop()] = ""
            
        return "".join(s_list)
        
