'''
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Note:

1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
'''
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1)>len(str2):
            str_len = len(str2)
            for i in range(str_len):
                div_len = str_len-i
                j = 0
                while j <= str_len-div_len:
                    div = str2[j:j+div_len]
                    j += 1
                    if div in str1 and div in str2:
                        if len(str1)%len(div) == 0 and len(str2)%len(div) == 0:
                            if len(div)>1:
                                return div
                            else:
                                return ""
        else:
            str_len = len(str1)
            for i in range(str_len):
                div_len = str_len-i
                j = 0
                while j <= str_len-div_len:
                    div = str2[j:j+div_len]
                    j += 1
                    if div in str1 and div in str2:
                        if len(str1)%len(div) == 0 and len(str2)%len(div) == 0:
                            if len(div)>1:
                                return div
                            else:
                                return ""
