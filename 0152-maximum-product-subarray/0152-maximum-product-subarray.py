class Solution:
    def maxProduct(self, nums: List[int]) -> int:
         max_pro = nums[0]
         max_ending_here = nums[0]
         min_ending_here = nums[0]

         for i in range(1, len(nums)):
            if nums[i] < 0:
                max_ending_here, min_ending_here = min_ending_here, max_ending_here

            max_ending_here = max(nums[i], max_ending_here * nums[i])
            min_ending_here = min(nums[i], min_ending_here * nums[i])

            max_pro = max(max_pro, max_ending_here)

         return max_pro
        