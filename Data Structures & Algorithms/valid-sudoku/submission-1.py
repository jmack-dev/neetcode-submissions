class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = board[i] 
            if not Solution.isValid(row):
                return False
            
            col = [row[i] for row in board]
            
            if not Solution.isValid(col):
                return False

            starting_row = (i // 3) * 3
            starting_col = (i % 3) * 3
            box = [board[starting_row + r][starting_col + c]  for c in range(3) for r in range(3)]
            
            if not Solution.isValid(box):
                return False

        return True
            

    def isValid(values: List[str]) -> bool:        
        seen = set()
        for v in values:
            if v != '.' and v in seen:
                return False
            seen.add(v)
        
        return True
        