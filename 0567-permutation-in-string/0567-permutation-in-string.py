class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        h1 = Counter(s1)
        h2 = Counter(s2[:n])

        if h1 == h2:
            return True

        for i in range(n, m):
            h2[s2[i]] += 1
            h2[s2[i-n]] -= 1

            if h2[s2[i-n]] == 0 :
                del h2[s2[i-n]]
            if h1 == h2:
                return True
            

        return False
        