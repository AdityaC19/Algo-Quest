class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        max_heap = []

        for key, val in counter.items():
            heapq.heappush(max_heap, (-val,key))
        
        ans = []
        prev_char, prev_freq = '', 0
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            ans.append(char)

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            prev_char, prev_freq = char, freq + 1
        
        return ''.join(ans) if len(ans) == len(s) else ""






        