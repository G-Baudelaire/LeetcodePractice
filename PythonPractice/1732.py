from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        largest = 0
        altitude = 0
        for i in gain:
            altitude += i
            if i > 0:
                largest = largest if largest >= altitude else altitude
        return largest
