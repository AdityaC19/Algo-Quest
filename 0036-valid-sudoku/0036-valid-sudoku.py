class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item == ".":
                    continue
                
                box_index = (i//3)*3 + (j//3)

                if item in row[i] or item in col[j] or item in box[box_index]:
                    return False

                row[i].add(item)
                col[j].add(item)
                box[box_index].add(item) 
        
        return True
        