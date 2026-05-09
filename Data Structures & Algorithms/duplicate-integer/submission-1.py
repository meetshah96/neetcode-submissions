class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        distinct_set = set()
        has_duplicate = False
        for i in nums:
            if i in distinct_set:
                has_duplicate = True
                break
            else:
                distinct_set.add(i)
        return has_duplicate