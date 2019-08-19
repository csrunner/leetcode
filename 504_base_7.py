'''
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
'''
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num>0:
            sign = 1
        elif num<0:
            sign = -1
        else:
            return '0'
        u_num = abs(num)
        output = 0
        counter = 1
        while u_num > 0:
            rem = u_num%7
            u_num = u_num/7
            output = counter*rem + output
            counter *= 10
            
        return str(sign*output)
