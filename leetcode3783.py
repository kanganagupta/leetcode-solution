class Solution:
    def mirrorDistance(self, n: int) -> int:
        copy = n
        rev = 0
        while copy>0:
            digits = copy%10
            rev = rev*10 + digits
            copy = copy//10
        return abs(n - rev)
        
