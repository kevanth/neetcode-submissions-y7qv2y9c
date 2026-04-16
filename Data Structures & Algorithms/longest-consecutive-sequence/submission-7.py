class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myDic = defaultdict(int)
        maxCount = 0
        for num in nums:
            if not myDic[num]:
                myDic[num] = myDic[num-1] + myDic[num+1] + 1
                myDic[num - myDic[num-1]] = myDic[num]
                myDic[num + myDic[num+1]] = myDic[num]
                maxCount = max(maxCount, myDic[num])
        return maxCount