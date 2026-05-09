class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_maps = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in num_maps:
                return [num_maps[diff], i]
            num_maps[v] = i