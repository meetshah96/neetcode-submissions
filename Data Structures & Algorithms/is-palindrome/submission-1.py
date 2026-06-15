class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [val.lower() for val in s if val != " " and val.isalnum() ]
        print(s)
        l = 0
        r = len(s) -1
        while l < r:
            if s[l] == s[r]:
                l +=1
                r -=1
            else:
                return False
        return True