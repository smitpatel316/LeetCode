class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True

        def dfs(i, j, k):
            if (
                i < 0
                or i >= len(board)
                or j < 0
                or j >= len(board[i])
                or k >= len(word)
                or word[k] != board[i][j]
            ):
                return False
            if k == len(word) - 1:
                return True
            tmp = board[i][j]
            board[i][j] = "#"
            res = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            )
            board[i][j] = tmp
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        return [word for word in words if self.exist(board, word)]
