class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        cursum=0

        for n in nums:
            if cursum<0:
                cursum=0
            cursum +=n
            maxSum=max(maxSum,cursum)
        return maxSum        