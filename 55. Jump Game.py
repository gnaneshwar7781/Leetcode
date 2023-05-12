class Solution(object):
    def canJump(self, nums):
        currentJumpValue=0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>currentJumpValue:
                currentJumpValue=0
            else:
                currentJumpValue+=1
        return currentJumpValue==0
        
