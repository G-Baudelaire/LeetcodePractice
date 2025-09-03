//
// Created by Germain Jones on 03/09/2025.
//

#ifndef SOLUTION151_H
#define SOLUTION151_H
#include <string>
#include <vector>

using std::string;

class Solution151 {
public:
  string reverseWords(string s) {
    std::string output;
    std::vector<std::string> strings;
    bool inWord = false;
    int start = 0;

    for (int i = 0; i < s.size(); i++) {
      bool isSpace = s[i] == ' ';
      if (inWord && isSpace) {
        strings.push_back(s.substr(start, i - start));
        inWord = false;
      }
      if (!inWord && !isSpace) {
        start = i;
        inWord = true;
      }
    }

    if (inWord) {
      strings.push_back(s.substr(start, s.size() - start));
    }

    for (size_t i = strings.size(); i > 0; i--) {
      if (!output.empty()) {
        output.append(" ");
      }
      output.append(strings[i - 1]); // fixed index
    }

    return output;
  }
};

#endif //SOLUTION151_H
