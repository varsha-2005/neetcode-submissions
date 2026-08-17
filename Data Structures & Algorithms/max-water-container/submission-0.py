class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        l,r=0,n-1
        maxi=0
        while l<r:
            ans=(r-l)*min(heights[l],heights[r])
            maxi=max(maxi,ans)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxi