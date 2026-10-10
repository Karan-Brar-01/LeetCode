class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        mx = -999999999999999999999
        for i in candies:
            if(i > mx):
                mx=i
        ans=[]
        for i in candies:
            if(mx-i <= extraCandies):
                ans.append(True)
            else:
                ans.append(False)
        return ans

        
        