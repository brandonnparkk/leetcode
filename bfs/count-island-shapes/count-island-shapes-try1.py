def count_distinct_islands(grid: List[List[int]]) -> int:
# 2-d grid
# lands = 1
# two islands have same shape IF translating one set of cells
# makes it equal the other
# rotations and reflections are valid distinct shapes
# 
# find definition of what translating is
    # same shape, but different location
# return num of distinct island shapes

# initially thinking BFS solution - going in all 4 directions fanning out.
# reminds me of num islands question

# ask clarifying questions
# if same shape, return 1
# can input be empty 2D list?
    # will not be empty
# can there be no islands? do we return 0?
    # will return 0
# what is max number of rows / cols?
    # 1 - 50
# what numbers can each cell be, only 0s and 1s?
    # either 0 or 1

# idea to implement
# create output variable to return at the end
# create directions list (left, right, up, down)
# create visited storage
# caveat: brute solution: go through each cell n times
    # o(N^2)
# loop through each item once - O(n) time complexity (use rows and cols)
# need to know if visited already
# more efficient solution is to use bfs
# creating a bfs helper function, calling that recursively
# create a queue, add to the queue before implementing bfs
# when island is found (end of bfs) - need to store the coords to figure out "shape"
# have some storage to hold each distinct islands "shape".
# as we finish bfs, then add to shapes list

# [(0,0), (0,1), (1,0)], [(0,3), (0,4), (1,3)]
# if find area of shape, won't work because rotations and reflections are valid
# something with the coords

# if we loop through each "shape", we use rows(r) / cols(c)
# (2-0, 5-0), (2-0, 5-1) = (2,5), (2,4)
# (2-0, 5-3), (2-0, 5-4) = (2,2), (2,1)
