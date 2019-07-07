'''
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False
'''
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A_counter = 0
        L_counter = 0
        for i in s:
            if i == 'A':
                A_counter += 1
                L_counter = 0
                if A_counter > 1:
                    return False
            elif i== 'L':
                L_counter += 1
                if L_counter > 2:
                    return False
            else:
                L_counter = 0
        return True
