class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        miss=1
        for x in nums:
            if x==miss:
                miss+=1
            elif x>miss:
                return miss
        return miss