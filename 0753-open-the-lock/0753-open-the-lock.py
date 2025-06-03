class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque(['0000'])
        seen = set()
        deadset = set(deadends)
        steps = 0

        def get_neighbors(combo):
            neighbors = []
            for i in range(4):
                digit = int(combo[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_combo = combo[:i] + str(new_digit) + combo[i+1:]
                    neighbors.append(new_combo)
            return neighbors
        
        if '0000' in deadset:
            return -1

        while q:
            for _ in range(len(q)):
                combination = q.popleft()
                if combination == target:
                    return steps
                for nei in get_neighbors(combination):
                    if nei not in deadset and nei not in seen:
                        q.append(nei)
                        seen.add(nei)
            steps += 1

        return -1


        
        