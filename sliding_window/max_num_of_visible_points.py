import math

def visiblePoints(points, angle, location):
     # convert coordinates to angles (radians)
        angles = []
        # if your location is the same as a coordinate
        same = 0
        x0, y0 = location
        for x, y in points:
            if x0 == x and y0 == y:
                same += 1
            else:
                # need to set y - y0 because 
                angles.append(math.degrees(math.atan2(y - y0, x - x0)))

        # sort the array
        angles.sort()
        # handle the wrap around logic because it's a circle. a degree can have 2 values (x, x + 360)
        angles += [a + 360 for a in angles]
        # sliding window to find the total number of visible points

        left = best = 0
        for right in range(len(angles)):
            #  can't use if because you might need more than one increment.
            while angles[right] - angles[left] > angle:
                left += 1
            # this gets number of visible points by calculating the "gap" between the left and right indexes.
            best = max(best, right - left + 1)

        return best + same