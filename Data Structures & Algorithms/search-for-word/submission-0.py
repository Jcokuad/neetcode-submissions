class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or #letter in word does not match letter in current board position
                (r, c) in path #visited same position twice
                ): 
                return False
            
            path.add((r, c))
            res = (dfs(r + 1, c, i + 1) or # add 1 to i since we found the letter we need
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1)) # looking at all four adjacent positions
            # if one returns true then it will continue in that direction

            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): # 0 for i since we are always starting at the beginning of the word
                    return True
                    
        return False


