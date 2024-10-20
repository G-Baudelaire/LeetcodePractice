import re
# Looking at solutions this can be done much more simply using .split and .join

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        left_pointer = 1
        stack = []

        path = re.sub(r"/+", "/", path)
        while left_pointer < len(path):
            match = re.match("[0-9A-z._]+", path[left_pointer:])

            if match.group() is None:
                left_pointer += 1
                continue
            if match.group() == ".":
                pass
            elif match.group() == "..":
                stack = stack[:-1]
            elif match.group():
                stack += [match.group()]

            left_pointer += match.end() + 1

        output = "/" if not stack else ""

        for s in stack:
            output += "/" + s

        return output
