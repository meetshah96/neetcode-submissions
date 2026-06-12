class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        l = 0
        window = list()
        for r in range(len(arr)):
            if r - l >= k:
                window.pop(0)
                l +=1
            window.append(arr[r])
            if len(window) == k:
                sumOfNum = 0
                for w in window:
                    sumOfNum +=w
                if (sumOfNum / k) >= threshold:
                    count +=1
        return count
