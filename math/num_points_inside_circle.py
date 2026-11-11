class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        # clarifying questions
        # are points that are on the borders count for inside a circle?
        # how big can points and queries be?
        # will points always have values
        # will queries always have values
        # can I have the formula to find area of a circle / points
            # thinking that I need the area of the circle relative to some coordinates
            # coords at (0,0) with area of 5
            # i think maybe not area...

        # idea to implement
        # loop through the queries
            # use the radius to find the "bounds" (pi * r^2 aka area), (2 * pi * r aka circumference?)
            # something to give the points some kind of "pi value"
            # my thought is that because it's a circle, I can't just check if coordinates of a point is in it like I can if it were a square.
            # is this something where I use an anchor? so I don't have to think of something "relative"
        # we'll need a counter for visible points in each "circle"\

        # circles = []
        output = []

        # for q in queries:
        #     curr_area = math.pi * q[-1]^2
        #     curr_circumference = 2*math.pi*q[-1]
        #     circles.append((curr_area, curr_circumference))
        
        # for circle in circles:
        #     for p in points:
        #         # does p exist in circle somehow
        #         # update output with num of points visible in circle
        #         # Idk this part of the solution

        # # I asked for a hint and was given this inequality
        # (x - h)^2 + (y - k)^2 > r^2

        # with this new given info, I'm thinking it will be an o(n^2) solution
        for qx, qy, qr in queries:
            counter = 0
            for px, py in points:
                # means points inside and also on the border of the circle
                if (px - qx)**2 + (py - qy)**2 <= qr**2:
                    counter += 1
            output.append(counter)
    
        return output