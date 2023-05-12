class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [ [0 for y in range(n)] for x in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] == 0: #无障碍
                dp[i][0] = 1
            else: #障碍后的全部为0
                break
        
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        for i in range(1,m,1):
            for j in range(1,n,1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        else:
            return dp[m-1][n-1]
