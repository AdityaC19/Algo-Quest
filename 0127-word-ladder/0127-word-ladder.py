from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        q = deque([beginWord])
        steps = 0

        while q:
            steps += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        tempWord = word[:i] + ch + word[i+1:]
                        if tempWord in wordSet:
                            wordSet.remove(tempWord)
                            q.append(tempWord)
            
        
        return 0
                        

