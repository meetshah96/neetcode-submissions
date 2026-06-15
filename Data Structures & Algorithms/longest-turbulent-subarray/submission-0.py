class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0,1
        res = 1
        pre = ""
        while r < len(arr):
            if arr[r-1] < arr[r] and pre != "<":
                res = max(res, r-l+1)
                pre = "<"
                r += 1
            elif arr[r-1] > arr[r] and pre != ">":
                res = max(res, r-l+1)
                pre = ">"
                r += 1
            else:
                r = r + 1 if arr[r] == arr[r-1] else r
                l = r-1
                pre = ""
        return res
