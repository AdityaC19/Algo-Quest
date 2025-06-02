class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        res = ""

        max_heap = [(-val, key) for key, val in counter.items()]
        heapq.heapify(max_heap)
        prev_char, prev_freq = '',0

        while max_heap:
            count, char = heapq.heappop(max_heap)
            res += char

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            prev_char, prev_freq = char, count + 1
        
        return res if len(s) == len(res) else ""











        