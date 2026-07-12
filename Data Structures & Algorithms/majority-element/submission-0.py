class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dic = {}

        for i in range(len(nums)):

            if nums[i] not in dic:

                dic[nums[i]] = 1
            
            else:

                dic[nums[i]] += 1
        
        for key,val in dic.items():

            if val > len(nums)//2:

                return key