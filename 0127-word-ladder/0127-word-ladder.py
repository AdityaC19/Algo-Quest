class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque([beginWord])
        seen = set()
        wordSet = set(wordList)
        count = 0

        while q:
            count += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for i in range(len(word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        temp = word[:i] + char + word[i+1:]
                        if temp in wordSet and temp not in seen:
                            seen.add(temp)
                            q.append(temp)
        return 0



        