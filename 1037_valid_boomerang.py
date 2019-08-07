'''
A boomerang is a set of 3 points that are all distinct and not in a straight line.

Given a list of three points in the plane, return whether these points are a boomerang.

 

Example 1:

Input: [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: [[1,1],[2,2],[3,3]]
Output: false
 

Note:

points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
'''
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        point0 = points[0]
        point1 = points[1]
        point2 = points[2]
        v1 = v2 = v3 =False
        k1 = k2 = k3 = 0
        if point0 == point1 or point0 == point2 or point1 == point2:
            return False
        
        try:
            k1 = (point0[1]-point1[1])/float((point0[0]-point1[0]))
        except :
            v1 = True
        try:
            k2 = (point0[1]-point2[1])/float((point0[0]-point2[0]))
        except :
            v2 = True
            
        try:
            k3 = (point1[1]-point2[1])/float((point1[0]-point2[0]))
        except :
            v2 = True
            
        if v1 and v2 and v3:
            return False
        if k1 == k2 and k1 == k3:
            return False
        return True
