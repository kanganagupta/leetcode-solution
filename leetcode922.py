class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:

        evens = []
        odds = []
        
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        
        res = []
        for i in range(len(nums)//2):
            res.append(evens[i])
            res.append(odds[i])
        
        return res
