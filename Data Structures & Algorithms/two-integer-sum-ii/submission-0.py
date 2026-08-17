class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq={}
        for i,num in enumerate(numbers):
            rem=target-num
            if rem in freq:
                return [freq[rem]+1,i+1]
            freq[num]=i
        return [-1,-1]
