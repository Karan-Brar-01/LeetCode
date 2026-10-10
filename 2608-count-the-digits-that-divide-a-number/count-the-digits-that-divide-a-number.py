class Solution:
    def countDigits(self, num: int) -> int:
        numstr=str(num)
        count =0
        for i in numstr:
            if(num % (int(i)) == 0):
                count += 1
        return count