//
// Created by germain on 01/10/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION283_H
#define LEETCODEPRACTICE_SOLUTION283_H
#include <vector>
#include <bits/forward_list.h>

class Solution {
public:
    void moveZeroes(std::vector<int> &nums) {
        int write = 0;
        for (int x : nums) if (x != 0) nums[write++] = x;
        std::fill(nums.begin() + write, nums.end(), 0);
    }
};
#endif //LEETCODEPRACTICE_SOLUTION283_H
