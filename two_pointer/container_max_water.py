class Solution:
    def max_area(self, heights: List[int]) -> int:
        # Your code goes here
        lp, rp = 0, len(heights) - 1
        max_area = 0

        while lp < rp:
            curr_width = rp - lp
            curr_height = min(heights[lp], heights[rp])
            curr_area = curr_width * curr_height
            max_area = max(max_area, curr_area)
            if heights[lp] < heights[rp]:
                lp += 1
            else:
                rp -= 1
        
        return max_area