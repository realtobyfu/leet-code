class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        output = []
        q = deque()
        l = r = 0

        while r < len(nums):

            if q and l > q[0]:
                q.popleft()

            # monotonously decreasing queue
            # we are going to store the index of nums in the output array
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)



            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output

