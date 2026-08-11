class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        for x in freq:
            if freq[x]>len(nums)//2:
                return x
        