'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # return str(int(num1)+int(num2))
        # return str((ord(num1)-ord('0'))+(ord(num2)-ord('0')))
        int_num1 = 0
        int_num2 = 0
        for i in num1:
            int_num1 = 10*int_num1+ord(i)-ord('0')
        for i in num2:
            int_num2 = 10*int_num2+ord(i)-ord('0')
        return str(int_num1+int_num2)
