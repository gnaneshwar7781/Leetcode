class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows, cols = len(board), len(board[0])

        visited = set()

        def dfs(i,r,c):
            if (i == len(word)):
                return True

            if (r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i] or (r,c) in visited):
                return False

            visited.add((r,c))

            res = (dfs(i+1,r+1,c) or
                   dfs(i+1,r-1,c) or
                   dfs(i+1,r, c-1) or
                   dfs(i+1,r, c+1))
            visited.remove((r,c))

            return res


        for r in range(rows):
            for c in range(cols):
                if dfs(0, r,c) : return True

        return False
