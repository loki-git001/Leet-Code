class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count = Counter(moves)
        return abs(count['R'] - count['L']) + count['_']