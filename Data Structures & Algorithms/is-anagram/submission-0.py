class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t = list(t)
        for val in s:
            for k,v in enumerate(t):
                found_match = False
                if val == v:
                    t.pop(k)
                    found_match = True
                    break
            if found_match == False:
                return False
            else:
                found_match = True
        return True
                