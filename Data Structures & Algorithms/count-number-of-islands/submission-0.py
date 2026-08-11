class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def solve(i,j):
            if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1'):
                return
            
            grid[i][j] ='D'
            solve(i+1,j)
            solve(i-1,j)
            solve(i,j+1)
            solve(i,j-1)

        count = 0
        for k in range(len(grid)):
            for l in range(len(grid[0])):
                if(grid[k][l]=='1'):
                    count+=1
                    solve(k,l)
        return count
        

