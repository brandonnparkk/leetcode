from typing import List

class Solution:
    def expand(self, s: str) -> List[str]:
        pass
        # phase 1: prase s into a list of sorted option lists
        groups = []
        i = 0
        while i < len(s):
            if s[i] == '{':
                j = s.index("}", i)
                options = s[i+1 : j].split(",")
                groups.append(sorted(options))
                i = j + 1
            else:
                groups.append([s[i]])
                i += 1

        # phase 2: backtrack, filling one position per level
        result = []
        path = []

        def dfs(pos: int) -> None:
            if pos == len(groups):
                # creates a new string each time
                # otherwise, we are just storing 4 references to the same list
                # at the end of the recursion, it's just an empty list.
                # creating a string, so that later changes don't affect it.
                result.append("".join(path))
                return
            for ch in groups[pos]:
                path.append(ch)
                # adds characters until hit the end of groups
                dfs(pos + 1)
                # remove the last character and bubbles up from there.
                path.pop()

        dfs(0)
        return result
