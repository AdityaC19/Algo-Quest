class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap = defaultdict(int)

        for i in magazine:
            hmap[i] += 1
        
        for note in ransomNote:
            if note in hmap and hmap[note] == 1:
                del hmap[note]
            elif note in hmap:
                hmap[note] -= 1
            else:
                return False
        
        return True