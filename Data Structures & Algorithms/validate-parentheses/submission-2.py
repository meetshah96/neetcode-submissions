class Solution:
    def remove(self):
        if self.stack:
            return self.stack.pop(-1)
        return

    def add(self, value):
        self.stack.append(value)
        return

    def isValid(self, s: str) -> bool:
        bracket_map = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        self.stack = []
        for bracket in s:
            if bracket in bracket_map.values():
                self.add(bracket)
            else:
                open_bracket = self.remove()
                if bracket_map.get(bracket) != open_bracket:
                    return False
        return True if len(self.stack) == 0 else False
