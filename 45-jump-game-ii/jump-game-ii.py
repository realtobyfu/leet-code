class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            # update the farthest point that can be reached
            farthest = max(farthest, i + nums[i])

            # when the current jumping range is exhausted
            # make another jump 
            if current_end == i:
                jumps += 1
                current_end = farthest
            
            if current_end >= n - 1:
                break

        return jumps

            
         