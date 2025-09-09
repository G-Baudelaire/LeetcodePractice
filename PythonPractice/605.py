from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for index in range(len(flowerbed)):
            # if flowerbed[index] == 1:
            #     continue

            left = index == 0 or flowerbed[index - 1] == 0
            right = index == len(flowerbed) - 1 or flowerbed[index + 1] == 0

            if left and right and flowerbed[index] == 0:
                flowerbed[index] = 1
                count += 1

        return n <= count
