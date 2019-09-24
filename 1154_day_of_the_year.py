'''
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61
 

Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.
'''
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        days = [31,28,31,30,31,30,31,31,30,31,30,31]
        date_split = date.split('-')
        year = int(date_split[0])
        month = int(date_split[1])
        day = int(date_split[2])
        if year%4 == 0:
            if year%100 == 0:
                if year%400 == 0:
                    days = [31,29,31,30,31,30,31,31,30,31,30,31]
            else:
                days = [31,29,31,30,31,30,31,31,30,31,30,31]
        output = 0
        for i in range(month-1):
            output += days[i]
        output += day
        return output
