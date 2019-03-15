'''
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.

'''
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        remainder_2 = n/2
        quotient_2 = n%2
        
        remainder_3 = n/3
        quotient_3 = n%3
        
        if quotient_2 == 1:
            output_2 = 2**(remainder_2-1)*3
        else:
            output_2 = 2**remainder_2
        
        if quotient_3 == 0:
            output_3 = 3**remainder_3
        elif quotient_3 == 1:
            output_3 = 3**(remainder_3-1)*4
        else:
            output_3 = 3**remainder_3*2
        
        return output_2 if output_2>output_3 else output_3
