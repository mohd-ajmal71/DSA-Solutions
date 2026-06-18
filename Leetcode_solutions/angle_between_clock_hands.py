class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        result = abs(30 * hour - 5.5 * minutes)

        if result > 180:
            result = 360 - result

        return result
