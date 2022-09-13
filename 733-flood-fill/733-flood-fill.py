class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_max, column_max = len(image), len(image[0])-1
        old_color = image[sr][sc]
        if old_color == color: return image
        
        def Fill(row, column):
            print(row, column)
            if image[row][column] == old_color:
                image[row][column] = color
                if row >= 1: Fill(row-1, column)
                if row+1 < row_max: Fill(row+1, column)
                if column >= 1: Fill(row, column-1)
                if column < column_max: Fill(row, column+1)
        Fill(sr, sc)
        return image