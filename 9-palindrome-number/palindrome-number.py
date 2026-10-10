class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx=str(x)
        n = len(strx)
        check=0
        for i in range(n//2):
            if(strx[i]!= strx[n-i-1]):
                check=1
                break
        if(check==1):
            return False 
        return True
        