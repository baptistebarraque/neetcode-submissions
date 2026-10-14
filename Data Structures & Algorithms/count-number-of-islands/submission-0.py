class Solution:

    def erase_adjacent(self, grid, i, j):
        if not(0<=i<len(grid)) or not(0<=j<len(grid[0])):
            return None
        if 0<=i<len(grid) and 0<=j<len(grid[0]):
            if grid[i][j]=='1':
                grid[i][j]='0'
                self.erase_adjacent(grid, i+1,j)
                self.erase_adjacent(grid, i,j+1)
                self.erase_adjacent(grid, i-1,j)
                self.erase_adjacent(grid, i,j-1)
        



    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    self.erase_adjacent(grid, i,j)
        return count

        