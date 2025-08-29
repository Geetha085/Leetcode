class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=[]
        nums.sort()
        for i in range(len(nums)-1):
           if nums[i+1] - nums[i] == 1:
              if nums[i] not in res:
                 res.append(nums[i])
              if nums[i+1] not in res:
                 res.append(nums[i+1])
        return len(res)

        