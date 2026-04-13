
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for ind,val in enumerate(nums):
            dic[val] = ind

        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums and dic[x] != i:
                return i, dic[x]
        
       
