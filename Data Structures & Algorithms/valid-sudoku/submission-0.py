class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] in seen and board[r][c] != '.':
                    return False
                seen.add(board[r][c])
        
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] in seen and board[r][c] != '.':
                    return False
                seen.add(board[r][c])
        
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                key = (r // 3, c // 3)
                if board[r][c] in boxes[key] and board[r][c] != '.':
                    return False
                boxes[key].add(board[r][c])
                
        
        return True