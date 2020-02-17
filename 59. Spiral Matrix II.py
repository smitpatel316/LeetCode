class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, left, bottom, right, counter = 0, 0, n-1, n-1, 0
        result = [None] * n
        for i in range(n):
            result[i] = [None] * n
        while True:
            if left > right:
                break
            for i in range(left, right+1):
                counter += 1
                result[top][i] = counter
            top += 1
            if top > bottom:
                break

            for i in range(top, bottom+1):
                counter += 1
                result[i][right] = counter
            right -= 1
            if right < left:
                break

            for i in range(right, left-1, -1):
                counter += 1
                result[bottom][i] = counter
            bottom -= 1

            if bottom < top:
                break

            for i in range(bottom, top-1, -1):
                counter += 1
                result[i][left] = counter
            left += 1
            if left > right:
                break
        return result