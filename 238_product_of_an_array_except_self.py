'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 1
        output = []
        for i in nums:
            total *= i
        for i in range(len(nums)):
            if nums[i] != 0:
                output.append(total/nums[i])
            else:
                tmp = 1
                for j in range(len(nums)):
                    if j != i:
                        tmp *= nums[j]
                output.append(tmp)
        return output
