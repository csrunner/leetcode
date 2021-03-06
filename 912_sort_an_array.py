'''
Given an array of integers nums, sort the array in ascending order.

 

Example 1:

Input: [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
'''
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        return nums
