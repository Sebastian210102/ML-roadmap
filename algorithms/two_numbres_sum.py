'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''


#My first solution that its an O(n^2)
def twoSum(self, nums: list[int], target: int) -> list[int]:
        
    for index in range(len(nums)):
         for index_2 in range(index+1, len(nums)):
            if (nums[index] + nums[index_2]) == target:
                return [index, index_2]
            


#Better time of solution 

def twoSum(self, nums: list[int], target: int) -> list[int]:
        
    dictionary = {
    }
    for i,number in enumerate(nums):
        com = target- number

        if com in dictionary:
            return [i,dictionary[com]]
        
        dictionary[number] = i

