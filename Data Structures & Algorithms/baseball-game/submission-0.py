class Solution:

    def get_score(self, count = 1):
        score = 0
        if count <= len(self.scores):
            for i in range(0, count):
                score += self.scores[-i - 1]
        return score
        
    def remove_score(self):
        if self.scores:
            self.scores.pop(-1)
        return
    
    def add_score(self, value):
        self.scores.append(value)
        return

    def calPoints(self, operations: List[str]) -> int:
        self.scores = []
        try:
            for ops in operations:
                if ops.lower() == "c":
                    self.remove_score()
                elif ops.lower() == "d":
                    score = self.get_score()
                    score += score
                    self.add_score(score)
                    print(self.scores)
                elif ops == "+":
                    score = self.get_score(2)
                    self.add_score(score)
                    print(self.scores)
                else:
                    ops = int(ops)
                    self.add_score(ops)

            print(self.scores)
            return sum(self.scores) if self.scores else 0
        except Exception as e:
            raise e
        
    