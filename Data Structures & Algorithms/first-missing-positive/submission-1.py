class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        missing = 1

        for x in nums:
            if x == missing:
                missing += 1
            elif x > missing:
                return missing

        return missing