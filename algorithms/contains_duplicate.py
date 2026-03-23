class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        set_nums = set(nums)

        if len(set_nums) < len(nums): 
            return True
        
        return False