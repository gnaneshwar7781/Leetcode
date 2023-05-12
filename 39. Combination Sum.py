class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        def backtrack(combination, start_index, target):
            if target == 0:
                result.append(combination)
                return
            for i in range(start_index, len(candidates)):
                candidate = candidates[i]
                if candidate > target:
                    break
                backtrack(combination + [candidate], i, target - candidate)
        backtrack([], 0, target)
        return result
