class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s = 'L' + dominoes + 'R'   # sentinels: every gap now has a push on both sides
        res = []
        i = 0                      # index of the last push seen
        for j in range(1, len(s)):
            if s[j] == '.':
                continue           # keep scanning for the next push
            gap = j - i - 1        # number of dots between s[i] and s[j]
            if i > 0:
                res.append(s[i])   # keep the real push at i (skip the left sentinel)
            if s[i] == s[j]:       # L...L or R...R: everything falls that way
                res.append(s[i] * gap)
            elif s[i] == 'L':      # L...R: pushes move apart, nothing changes
                res.append('.' * gap)
            else:                  # R...L: meet in the middle
                half = gap // 2
                res.append('R' * half + '.' * (gap % 2) + 'L' * half)
            i = j
        return ''.join(res)        # right sentinel is never appended