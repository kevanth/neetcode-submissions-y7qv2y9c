class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}
        for num in nums:
            if num not in numsDict:
                numsDict[num] = "True"
            else:
                return True
        return False