class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n=len(people)
        boat,l,r=0,0,n-1
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1           
            r-=1
            boat+=1
        return boat