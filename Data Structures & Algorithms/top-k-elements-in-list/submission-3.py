class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        app=[]
        for x in nums:
            freq[x]=freq.get(x,0)+1
        app=sorted(freq,key=freq.get,reverse=True)
        return app[:k]
