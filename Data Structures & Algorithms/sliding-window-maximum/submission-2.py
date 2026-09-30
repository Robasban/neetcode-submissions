class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        for i in range(k):
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
            
        res = []
        l = 0
        for r in range(k, len(nums)):
            res.append(nums[deque[0]])
            if deque[0] == l:
                deque.popleft()
            while deque and nums[deque[-1]] < nums[r]:
                deque.pop()
            deque.append(r)
            l += 1
        res.append(nums[deque[0]])
        return res