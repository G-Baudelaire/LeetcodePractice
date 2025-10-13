//
// Created by germain on 13/10/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION67_H
#define LEETCODEPRACTICE_SOLUTION67_H

#include <string>
using std::string;

class Solution {
public:
    string addBinary(string a, string b) {
        if (a.size() < b.size()) {
            string &short_string = a, &long_string = b;
        } else {
            string &short_string = b, &long_string = a;
        }
        bool carry = true;
        string result(a.size() + 1, '0');


    }
};
#endif //LEETCODEPRACTICE_SOLUTION67_H
