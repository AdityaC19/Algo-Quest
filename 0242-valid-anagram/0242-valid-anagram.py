class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ds = Counter(s)
        # dt = Counter(t)

        # return ds == dt

        ds = defaultdict(int)
        dt = defaultdict(int)

        for i in s:
            ds[i] += 1

        for i in t:
            dt[i] += 1

        return ds == dt





        