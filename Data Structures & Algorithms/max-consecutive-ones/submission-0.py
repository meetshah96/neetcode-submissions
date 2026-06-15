class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxCounter = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                maxCounter = max(maxCounter, r-l+1)
            else:
                l = r + 1
        return maxCounter