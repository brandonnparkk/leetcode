class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        #  clarifying questions
        # how big can house be?
        # how big can heaters be?
        # how big are the items within the list?
        # houses is sorted in increasing order, same with heaters, is this the case?
        # is there a case where the output could be 0, house and heater is 1?

        h he x x h
        1  2 3 4 5

        # figure out the max length, which will give the min radius
        # how far apart is a heater to a house
        # based off the contrainsts, thinking of O(n) or O(logn) as the time complexity

        # idea for implementation
        # if we think about this as find all the heaters
        # thinking of what kind of ds or algo to use here...
        # go left as far until you find a house
        # go right as far until you find a house
        # get max of left-distance, right-distance
        # keep doing this check until you loop through all heaters 
        # thinking this is some kind of array problem?

        # implementation
        max = 0

        for i in range(len(heaters)):
            heater_loc = heaters[i]
            steps_left = 0
            steps_right = 0

            # i feel like it's something where we combine the two lists?

            # check left
            while heater_loc - steps_left != houses[heater_l]
            # check right
            # get max of steps_left, steps_right
        
        # return max?


        # Solution here
        # houses.sort()
        heaters.sort()
        radius = 0
        for house in houses:
            left, right = 0, len(heaters) - 1
            while left < right:
                mid = (left + right) // 2
                # this check is what makes it so that we find the heater to the right
                # we are always increasing the right side
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid
            # after binary search, it finds the heater to the 'right' of the house
            dist = abs(heaters[left] - house)
            # this is a boundary check, there's no heater to the left, because it's at the start
            # only finding the heater to the 'left' if it's possible.
            if left > 0:
                # this finds the nearest heater to the left, that's why we have left - 1
                dist = min(dist, abs(heaters[left - 1] - house))
            radius = max(radius, dist)
        return radius