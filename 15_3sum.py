'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = list()
        sort_solution = list()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                
                for l in range(j+1,len(nums)):
                    
                    if nums[i]+nums[j]+nums[l] == 0:
                        sorted = [nums[i],nums[j],nums[l]]
                        sorted.sort()
                        if sorted not in sort_solution:
                            solution.append([nums[i],nums[j],nums[l]])
                            sort_solution.append(sorted)
                            
        return solution                    
        
