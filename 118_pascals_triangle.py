'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        tri = [[1],[1,1]]
        previous = [1,1]
        
        for i in range(3,numRows+1):
            current = [1]
            for j in range(len(previous)-1):
                current.append(previous[j]+previous[j+1])
            current.append(1)
            previous = current
            tri.append(current)
        return tri
