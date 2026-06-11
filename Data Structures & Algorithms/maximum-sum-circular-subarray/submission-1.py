class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if not nums:
            return None
        globalMax, globalMin  = nums[0], nums[0]
        currMax, currMin = 0, 0
        totalSum = 0

        for n in nums:
            totalSum +=n
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)

        return max(globalMax, totalSum - globalMin) if globalMax > 0 else globalMax