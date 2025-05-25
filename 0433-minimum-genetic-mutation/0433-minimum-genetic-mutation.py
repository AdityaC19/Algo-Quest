class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque([startGene])
        bankset = set(bank)
        seen = set([startGene])
        steps = 0

        if endGene not in bankset:
            return -1

        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endGene:
                    return steps
                for i in range(len(word)):
                    for ch in 'ACGT':   # only check for these gene choices
                        mutation = word[:i] + ch + word[i+1:]
                        if mutation in bankset and mutation not in seen:
                            q.append(mutation)
                            seen.add(mutation)
            steps += 1
        
        return -1




        