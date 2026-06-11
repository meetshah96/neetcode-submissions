class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None

        maxSum = nums[0]
        currSum = 0

        for n in nums:
            currSum = max(currSum, 0) + n
            maxSum = max(currSum, maxSum)
        return maxSum