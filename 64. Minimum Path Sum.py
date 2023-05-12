
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        mem=[[0]*n for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    mem[i][j]=grid[-1][-1]
                elif i==m-1 and j!=n-1 :
                    mem[i][j]=grid[i][j]+mem[i][j+1]
                elif j==n-1 and i!=m-1:
                    mem[i][j]=grid[i][j]+mem[i+1][j]
                elif i<m-1 and j<n-1 :    
                    mem[i][j]=grid[i][j]+min(mem[i+1][j],mem[i][j+1])
        return mem[0][0]



       
       
  
        
