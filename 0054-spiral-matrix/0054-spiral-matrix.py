class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        result = []
        i, j = 0, 0

        RIGHT, DOWN, LEFT, UP = 0,1,2,3
        direction = RIGHT

        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1
        UP_WALL = 0

        while len(result) != m*n:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    result.append(matrix[i][j])
                    j+=1
                i, j = i+1, j-1
                RIGHT_WALL -= 1
                direction = DOWN
            
            elif direction == DOWN:
                while i < DOWN_WALL:
                    result.append(matrix[i][j])
                    i+=1
                i,j = i-1, j-1
                DOWN_WALL -= 1
                direction = LEFT

            elif direction == LEFT:
                while j > LEFT_WALL:
                    result.append(matrix[i][j])
                    j-=1
                i,j = i-1,j+1
                LEFT_WALL += 1
                direction = UP
            
            elif direction == UP:
                while i > UP_WALL:
                    result.append(matrix[i][j])
                    i-=1
                i,j = i+1,j+1
                UP_WALL += 1
                direction = RIGHT
    
        return result
