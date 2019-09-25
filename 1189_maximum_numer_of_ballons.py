'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
'''
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        word_l = ['b','a','l','o','n']
        word_c = [0]*5
        for t in text:
            if t in word_l:
                if t == 'b':
                    word_c[0] += 1
                elif t == 'a':
                    word_c[1] += 1
                elif t == 'l':
                    word_c[2] += 0.5
                elif t == 'o':
                    word_c[3] += 0.5
                else:
                    word_c[4] += 1
        mini = word_c[0]
        for c in word_c:
            if c<mini:
                mini=c
        return int(mini)
