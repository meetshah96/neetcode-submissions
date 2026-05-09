class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return
        output = [0]
        start_point = 1
        while True:
            for n in range(start_point, len(nums)):
                sum = nums[output[0]] + nums[n]
                if sum == target:
                    output.append(n)
                    break
            if len(output) == 2:
                break
            output = [start_point]
            start_point = start_point +1
        return output