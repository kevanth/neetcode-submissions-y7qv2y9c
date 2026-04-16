class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myDic = {}
        maxCount = 0
        nums = sorted(nums)
        for num in nums:
            if num-1 in myDic:
                myDic[num] = myDic[num-1] + 1
                if maxCount < myDic[num]:
                    maxCount = myDic[num]
            else:
                myDic[num] = 1
                if maxCount < myDic[num]:
                    maxCount = myDic[num]
        return maxCount