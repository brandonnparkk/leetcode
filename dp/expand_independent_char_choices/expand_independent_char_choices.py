from typing import List

class Solution:
    def expand(self, s: str) -> List[str]:
        pass
        # clarifying questions:
        # what are the constraints on the parameter?
        # can the result be in any order?
        # if the word is the same, is that ok, or do I have to filter out same words?
        # if len s is 0, then return an empty list?
        # brackets are the only delimiter, (open and close)
        # the number of chars in each bracket segment is variable and doesn't have to be the same numbers

        # thinking immediately because we are looking at combinations, that we use some kind of backtracking
        # also thinking through looping through the items in the string
        # definitely won't work to just do nested loops for this solution, it will time out

        # need to think of a way to handle this in o(n) time so it stays in one loop
        # thinking of a way to loop through each "bracket" and think of them as lists
        # then, just get the max len and just loop by that, not sure what to do here...

        # what does backtracking use, some sort of start index?
        # backtracking, you use sorting, so we sort each of the bracket segments
        