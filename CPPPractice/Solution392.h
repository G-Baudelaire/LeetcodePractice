//
// Created by Germain Jones on 13/08/2025.
//

#ifndef LEETCODEPRACTICE_SOLUTION392_H
#define LEETCODEPRACTICE_SOLUTION392_H
#include <string>
using std::string;

class Solution {
public:
  bool isSubsequence(string s, string t) {
    int index_s, index_t;

    for (index_s = 0, index_t = 0; index_s < s.size() && index_t < t.size();
         index_t++) {
      if (s[index_s] == t[index_t]) index_s++;
    }

    return index_s == s.size();
  }
};

#endif //LEETCODEPRACTICE_SOLUTION392_H
