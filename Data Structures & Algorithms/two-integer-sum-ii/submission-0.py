class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while True:
            lNum = numbers[l]
            rNum = numbers[r]
            if lNum + rNum == target:
                return [l + 1,r + 1]
            elif lNum + rNum < target:
                l += 1
            else:
                r -= 1
        return ret
