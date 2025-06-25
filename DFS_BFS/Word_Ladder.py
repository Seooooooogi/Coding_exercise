from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        q = deque([(beginWord, 1)])
        # 해싱을 이용
        word_set = set(wordList)
        visited = set()
        while q:
            cur_word, output = q.popleft()
            visited.add(cur_word)
            for i in range(len(cur_word)):
                # wordlist에서 찾지 말고 모든 경우의 수를 현재 word 안에서 찾는 것이 더 빠름
                for next_str in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = cur_word[:i] + next_str + cur_word[i+1:]
                    if next_word == endWord:
                        return output + 1
                    # 해싱을 이용하여 전체 순회를 하지 말고 빠르게 검색
                    if next_word not in visited and next_word in word_set:
                        visited.add(next_word)
                        q.append((next_word, output+1))
                
        return 0
        
