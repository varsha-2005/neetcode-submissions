class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq={}
        app=[]
        for x in nums:
            freq[x]=freq.get(x,0)+1
        for x,y in freq.items():
            if y>len(nums)//3:
                app.append(x)
        return app