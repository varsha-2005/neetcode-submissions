class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def search(piles,mid):
            cnt=0
            for x in piles:
                cnt+=math.ceil(x/mid)
            return cnt
        n=max(piles)
        low,high=1,n
        ans=n
        while low<=high:
            mid=(low+high)//2
            hrs=search(piles,mid)
            if hrs<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans