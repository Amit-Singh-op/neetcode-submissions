class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def solve(i,j, cache={}):
            if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1' or (i,j) in cache):
                return 0
            
            grid[i][j] ='D'
            cache[(i,j)] = solve(i+1,j, cache) or solve(i-1,j, cache) or solve(i,j+1, cache) or solve(i,j-1, cache)
            return cache[(i,j)]

        count = 0
        for k in range(len(grid)):
            for l in range(len(grid[0])):
                if(grid[k][l]=='1'):
                    count+=1
                    solve(k,l)
        return count
        

