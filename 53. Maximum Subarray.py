class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_end_here=0
        max_so_far=0
        for i in range (len(nums)):
            max_end_here=max_end_here+nums[i]
            if max_so_far<max_end_here:
                max_so_far=max_end_here
            if max_end_here<0:
                max_end_here=0
        if max_so_far>0:
            return max_so_far
        else:
            return max(nums)
