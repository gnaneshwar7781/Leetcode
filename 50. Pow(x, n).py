class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n > 0:
            res = x
        if n < 0:
            res = 1/x
        answer = 1
        bin_n = bin(abs(n))
        for char in reversed(bin_n[2:]):
            print( int(char))
            if int(char):
                answer = answer * res
            res *= res

        return answer
