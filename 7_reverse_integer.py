'''
Given a 32-bit signed integer, reverse digits of an integer.
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.x = x
        if self.x>2**31-1 or self.x<-2**31:
            return 0
        else:
            str_x = str(self.x)
            rev_x = ''
            ori_len = len(str(self.x))
            abs_len = len(str(abs(self.x)))
            x_len = len(str(self.x))
            sign = 1
            if ori_len == abs_len:
                x_len = x_len
            else:
                x_len = x_len-1
                sign = -1
            for i in range(x_len):
                rev_x += str_x[-i-1]
            output = sign*int(rev_x)
            if output > 2**31-1 or output < -2**31:
                return 0
            else:
                return output
