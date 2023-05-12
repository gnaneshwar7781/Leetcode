class Solution(object):
    def reverse(self, x):
        ans=0
        temp=0
        if(x<0):
            x=abs(x)
            temp=1
        while(x>0):
            r=x%10
            x=x//10
            ans=(ans*10)+r
        if(ans>(2**31)-1 ):
            return 0
        if(temp):
            return -ans
        return ans
