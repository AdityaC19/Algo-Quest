class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([startGene])
        bankset = set(bank)
        seen = set([startGene])
        steps = 0

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endGene:
                    return steps
                for i in range(len(word)):
                    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        temp = word[:i] + ch + word[i+1:]
                        #print(temp)
                        if temp in bankset and temp not in seen:
                            q.append(temp)
                            seen.add(temp)
            steps += 1
        
        return -1




        