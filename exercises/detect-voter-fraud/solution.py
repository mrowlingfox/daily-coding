class Solution:
    def solve(self, votes):
        return len({v for _, v in votes}) != len(votes)