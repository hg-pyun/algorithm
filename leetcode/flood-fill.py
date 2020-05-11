class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        initColor = image[sr][sc]
        
        def dfs(image, sr, sc, newColor):
            if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1:
                return image

            nonlocal initColor
            if image[sr][sc] == newColor or image[sr][sc] != initColor:
                return image

            image[sr][sc] = newColor

            dfs(image, sr + 1, sc, newColor)
            dfs(image, sr -1, sc, newColor)
            dfs(image, sr, sc + 1, newColor)
            dfs(image, sr, sc - 1, newColor)
        
        dfs(image, sr, sc, newColor)
        
        return image
