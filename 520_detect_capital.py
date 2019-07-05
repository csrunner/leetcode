'''
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True
 

Example 2:

Input: "FlaG"
Output: False
'''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        follow_small = False
        follow_big = False
        if ord(word[0])>=ord('A') and ord(word[0])<=ord('Z'):
            for i in range(1,len(word)):
                if ord(word[i])>=ord('a'):
                    follow_small = True
                    if follow_big:
                        return False
                if ord(word[i])<=ord('Z'):
                    follow_big = True
                    if follow_small:
                        return False
            return True
        else:
            for i in range(1,len(word)):
                if ord(word[i])<=ord('Z'):
                    return False
            return True
            
                
        
