class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while i < (len(nums)):
            a = nums.count(nums[i])

            if a == 1:
                i+=1
                continue

            elif a > 2:
                for _ in range(a-2):
                    nums.pop(i)
            i += 2

        return len(nums)
