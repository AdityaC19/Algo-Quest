class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            #print(sorted_s)
            if sorted_s in grp:
                grp[sorted_s].append(s)
            else:
                grp[sorted_s] = [s]
        
        return [val for val in grp.values()]
