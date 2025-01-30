from typing import List


class Solution:
    ORD_OF_A = ord("a")

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()

        for string in strs:
            characters = [0] * 26
            self.tally_characters(string, characters)
            self.add_string_to_hashmap(hashmap, string, characters)

    def tally_characters(self, string, characters):
        for char in string:
            characters[ord(char) - Solution.ORD_OF_A] += 1
            

    def add_string_to_hashmap(self, hashmap, string, characters):
        if characters in hashmap:
            hashmap[characters].append(string)
        else:
            hashmap[characters] = [string]
