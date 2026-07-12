class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dic = {}

        for i in range(len(nums)):

            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]]+=1
            
        for key,val in dic.items():

            if val > 1:
                return True
        return False