import heapq

def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
    heap = []
    for i in range(len(points)):
        x, y = points[i]
        distance = x * x + y * y

        heapq.heappush(heap, (-distance, i))
        if len(heap) > k:
            heapq.heappop(heap)

    return [points[p[i]] for p in heap]
