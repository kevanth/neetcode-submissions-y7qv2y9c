class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myDic = defaultdict(int)
        maxCount = 0
        for num in nums:
            if num in myDic and myDic[num] > 0:
                continue
            myDic[num] = myDic[num-1] + myDic[num+1] + 1
            if myDic[num - myDic[num-1]] > 0 :
                myDic[num - myDic[num-1]] = myDic[num]
            if myDic[num + myDic[num+1]] > 0 :
                myDic[num + myDic[num+1]] = myDic[num]
            maxCount = max(maxCount, myDic[num])
        return maxCount