class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for i in range(len(points)):
            minHeap.append([points[i][0] ** 2 + points[i][1] ** 2, points[i]])

        heapq.heapify(minHeap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])

        return res