class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDic = {}
        maxArr = [[0,0] for _ in range(k)]
        currMax = [0] * k
        for i in range(len(nums)):
            if nums[i] in myDic:
                myDic[nums[i]] += 1
            else:
                myDic[nums[i]] = 1
            newCount = myDic[nums[i]]
            j = 0
            for thisMax in maxArr:
                if thisMax[1] < newCount and nums[i] not in currMax:
                    thisMax[0] = nums[i]
                    thisMax[1] = newCount
                    currMax[j] = nums[i]
                    break
                elif thisMax[1] < newCount and nums[i] == thisMax[0]:
                    thisMax[1] = newCount
                    break
                j += 1
                print(maxArr)
        cleanUp = []
        for thisMax in maxArr:
            cleanUp.append(thisMax[0])

        return cleanUp