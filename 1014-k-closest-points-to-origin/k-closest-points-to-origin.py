import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)


        # def distance(x, y):
        #     return x^2 + y^2

        # heap = []
        # for x, y in points:
        #     d = -distance(x, y)
        #     if len(heap) < k:
        #         heapq.heappush(heap, (d, x, y))

        #     else:
        #         if d > heap[0][0]:
        #             heapq.heappushpop(heap, (d, x, y))

        # return [(x, y) for _, x, y in heap]

        