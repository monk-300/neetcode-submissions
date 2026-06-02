class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newMap = {}
        for k, v in enumerate(nums):
            diff = target - nums[k]
            if diff in newMap:
                return [newMap[diff], k]
            else:
                newMap[v] = k