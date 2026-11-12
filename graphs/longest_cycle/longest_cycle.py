from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        # functional graph (think of linked lists, they go in one direction)
        # learn to spot 'functional graphs'
        # if problem asks "each node has at most one outgoing edge"
        # or if "each element points to one next element"

        # Kahn's topological sort

        visit_step = {}
        step = 0
        longest = -1

        for start in range(len(edges)):
            if start in visit_step:
                continue # already handled in earlier walk

            walk_start = step # steps >= this belong to THIS walk
            node = start

            # walk forward until a dead end or a node we've seen before
            while node != -1 and node not in visit_step:
                visit_step[node] = step
                step += 1
                node = edges[node]

            # detect a cycle
            if node != -1 and visit_step[node] >= walk_start:
                longest = max(longest, step - visit_step[node])

        return longest