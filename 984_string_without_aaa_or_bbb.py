'''
Given two integers A and B, return any string S such that:

S has length A + B and contains exactly A 'a' letters, and exactly B 'b' letters;
The substring 'aaa' does not occur in S;
The substring 'bbb' does not occur in S.
 

Example 1:

Input: A = 1, B = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: A = 4, B = 1
Output: "aabaa"

'''
class Solution(object):
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        output = ''
        A_str = list(A*'a')
        B_str = list(B*'b')
        while len(A_str)>len(B_str):
            if len(B_str)>0:
                A_str.pop()
                output += 'a'
                A_str.pop()
                output += 'a'
                B_str.pop()
                output += 'b'
            else:
                while A_str:
                    A_str.pop()
                    output += 'a'
                return output
        
            
        while len(A_str)<len(B_str):
            if len(A_str)>0:
                B_str.pop()
                output += 'b'
                B_str.pop()
                output += 'b'
                A_str.pop()
                output += 'a'
            else:
                while B_str:
                    B_str.pop()
                    output += 'b'
                return output
        while B_str:
            A_str.pop()
            output += 'a'
            B_str.pop()
            output += 'b'
        return output
