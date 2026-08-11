class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # return nums
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]<nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        return nums
