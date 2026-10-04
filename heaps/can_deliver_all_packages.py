import heapq

def canDeliverAllPackages(truckCapabilities, packageWeights):
    results = []
    for trucks, packages in zip(truckCapabilities, packageWeights):
        packages.sort(reverse = True)
        max_heap = [-cap for cap in trucks]
        heapq.heapify(max_heap)

        feasible = True
        for weight in packages:
            if not max_heap:
                feasible = False
                break

            best_capacity = -heapq.heappop(max_heap)
            if best_capacity < weight:
                feasible = False
                break

            new_capacity = best_capacity // 2
            if new_capacity > 0:
                heapq.heappush(max_heap, -new_capacity)

        results.append(1 if feasible else 0)
    return results