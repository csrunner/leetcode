'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        index = []
        for i in range(len(nums)):
            if nums[i] == 0:
                index.append(i)
        counter = 0
        for ind in index:
            del nums[ind-counter]
            counter += 1
            
        for _ in range(len(index)):
            nums.append(0)
