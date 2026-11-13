import math

def visiblePoints(points, angle, location):
    # set origin using location
    lx, ly = location
    angles = []
    max_points = 0

    for x, y in points:
        # point relative to origin
        cx, cy = x - lx, y - ly
        if cx == 0 and cy == 0:
            max_points += 1
            continue
        angles.append(math.degrees(math.atan2(cx, cy)))

    angles.sort()
    # why are we sorting?
    angles += [a + 360 for a in angles]
    # why add 360, because we are using atan which returns a value -180 to 180
    # adding 360 allows us get a contiguous array of positive values, which we'll use in the sliding window
    # if there were negatives, it would incorrectly set values far apart, even though on a circle, the difference is small
        # i.e. -170 and 170. the difference is only 20 degrees.
    # does sorting first matter? should we sort after the adding 360?

    left = best = 0
    for right in range(len(angles)):
        # confused about this while, wouldn't angles[right] be equal to angles[left] for the first iteration?
        while angles[right] - angles[left] > angle:
            # we are making the angle smaller
            left += 1
        # why are we adding 1? I know it's right, but need to understand the explanation
        best = max(best, right - left + 1)

    return best + max_points


    