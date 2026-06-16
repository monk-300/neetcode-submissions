class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newHashMap = {}
        for k, v in enumerate(nums):
            diff = target - nums[k]
            if diff in newHashMap:
                return [newHashMap[diff], k]
            else:
                newHashMap[v] = k