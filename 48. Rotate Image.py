class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()
        for i in range(0,n):
            lisa = []
            for j in range(0,n):
                lis = matrix[j]
                lisa.append(lis[i])
                if lisa not in matrix:
                    matrix.append(lisa)
        if(n!=1):
            for i in range(0,n):
                matrix.pop(0)
