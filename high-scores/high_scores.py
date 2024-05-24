class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def scores(self):
        return self.scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        sorted_scores = sorted(self.scores, reverse=True)

        return sorted_scores[:3]
