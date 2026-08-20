class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def capa(weights,mid):
            curr=0
            day=1
            for w in weights:
                if curr+w >mid:
                    day+=1
                    curr=w
                else:
                    curr+=w
            return day
        low=max(weights)
        ans=-1
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            nof=capa(weights,mid)
            if nof<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans