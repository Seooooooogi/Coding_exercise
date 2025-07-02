class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word, pat):
            map_w = [0] * 128
            map_p = [0] * 128
            for i, (w, p) in enumerate(zip(word, pat), 1):
                if map_w[ord(w)] != map_p[ord(p)]:
                    print(w, map_w[ord(w)], p, map_p[ord(p)])
                    return False
                map_w[ord(w)] = map_p[ord(p)] = i
            return True
            
        return [w for w in words if match(w, pattern)]
        
