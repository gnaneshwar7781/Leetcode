import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res=collections.defaultdict(list)
        for i in strs:
            res[tuple(sorted(i))].append(i)
        return res.values()
