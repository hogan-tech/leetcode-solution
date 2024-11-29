class Solution(object):
    def floodFill(self, image, sr, sc, color):
        R, C = len(image), len(image[0])
        oldColor = image[sr][sc]
        if oldColor == color:
            return image

        def dfs(r, c):
            if image[r][c] == oldColor:
                image[r][c] = color
                if r >= 1:
                    dfs(r-1, c)
                if r+1 < R:
                    dfs(r+1, c)
                if c >= 1:
                    dfs(r, c-1)
                if c+1 < C:
                    dfs(r, c+1)
        dfs(sr, sc)
        return image