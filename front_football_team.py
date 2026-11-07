class Solution:
  def chooseFrontTeam(self, teamA: List[int], teamB: List[int]) -> str:
    # clarifying questions
    # thinking right off the bat here...
    # loop using the max length of both lists
    # loop through each one and check if the difference is negative, if a == True, do nothing. else, set a to False, early return
    # if negative, if b != False, set to False, early return else, set to True,
    # if one team is empty, can only be either if one of the teams is empty.
    # set as impossible first - base case?
    # storage variable will be an object
    # {
    #   a: True
    #   b: False
    #   c: Either
    # }
    
    # then, go through all the values in the object, and return the key that has a True value

    # thinking the hint is something about having sorted lists
    # if using a loop and inner loop, this is o(n^2) and it won't be fast enough, especially with the constraints given.

    team_a_sorted = sorted(teamA)
    team_b_sorted = sorted(teamB)

    a_front = b_front = True

    for x,y  in zip(team_a_sorted, team_b_sorted):
        if x >= y:
            a_front = False
        if y >= x:
            b_front = False
        if not a_front and not b_front:
           return 'IMPOSSIBLE'

    if a_front and b_front:
       return 'Either'
    return 'A' if a_front else 'B'