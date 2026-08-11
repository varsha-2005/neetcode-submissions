class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        prefixSum=0
        cnt=0
        for x in nums:
            prefixSum+=x
            rem=prefixSum-k
            if rem in freq:
                cnt+=freq[rem]
            freq[prefixSum]=freq.get(prefixSum,0)+1
        return cnt






        # cnt=0
        # for i in range(len(nums)):
        #     tot=0
        #     for j in range(i,len(nums)):
        #         tot+=nums[j]
        #         if tot==k:
        #             cnt+=1
        # return cnt