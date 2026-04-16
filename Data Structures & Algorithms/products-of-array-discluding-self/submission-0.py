class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(math.prod(nums[0:i]) * math.prod(nums[i+1:]))
        return output