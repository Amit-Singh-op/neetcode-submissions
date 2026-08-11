class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def solve(i,j, cur = 0):
            if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!=1):
                return 0
            
            grid[i][j]=-1
            return 1+ solve(i+1, j, cur+1) + solve(i-1,j, cur+1) + solve(i, j+1, cur+1)+solve(i,j-1, cur+1)
        count = 0
        for k in range(len(grid)):
            for l in range(len(grid[0])):
                if(grid[k][l]==1):
                    count = max(solve(k,l), count)
                    print(count)

        return count


        
        
        