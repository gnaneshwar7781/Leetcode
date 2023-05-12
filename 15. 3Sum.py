class Solution:
    def threeSum(self, nums):
        n=len(nums)
        a=[]
        nums.sort()
        for i in range(n):
            l,r = i+1, n-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    b=[nums[i],nums[l],nums[r]]
                    if b not in a:
                        a.append(b)
                    l+=1               
        return a
