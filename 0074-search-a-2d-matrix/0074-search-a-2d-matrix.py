class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l = 0
        r = m*n-1

        while l <= r:
            mid = l + ((r-l)//2)

            # In a 2d m*n matrix
            # row = mid/n
            # col = mid%n

            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False



        

        

        