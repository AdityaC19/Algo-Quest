class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x):
            return x[0] * x[0] + x[1] * x[1]
        
        return sorted(points, key=distance)[:k]

