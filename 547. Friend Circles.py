class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        seen = set()

        def dfs(you):
            for class_mate, is_friend in enumerate(M[you]):
                if is_friend and class_mate not in seen:
                    seen.add(class_mate)
                    dfs(class_mate)

        friend_circles = 0
        for i in range(len(M)):
            if i not in seen:
                dfs(i)
                friend_circles += 1
        return friend_circles
