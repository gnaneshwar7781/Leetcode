class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        num = [j for j in range(1,n+1)]

        result = []

        subarr = []

        def dfs(i):
            if len(subarr) == k:
                result.append(subarr[:])
                # subarr = []
                return

            if i >= len(num):
                return

            subarr.append(num[i])
            dfs(i+1)
            subarr.pop()
            dfs(i+1)

        dfs(0)

        return result
