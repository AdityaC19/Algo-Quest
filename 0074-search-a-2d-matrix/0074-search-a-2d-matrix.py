class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        l = 0
        r = m*n-1

        while l <= r:
            mid = l+(r-l)//2
            mid_i =  mid// n
            mid_j = mid % n
            m = matrix[mid_i][mid_j]

            if m == target:
                return True
            if m > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False