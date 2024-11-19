class InitialSolution:
    def majorityElement(self, nums: List[int]) -> int:
        tally = dict()
        majority_number = int(len(nums) / 2)
        for i in nums:
            try:
                tally[i] += 1
            except KeyError:
                tally[i] = 1

            if majority_number < tally[i]:
                return i


# Solution using moore voting algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = None

        for i in nums:
            if element == i:
                count += 1
            elif count == 0:
                element = i
                count += 1
            else:
                count -= 1

        return element
