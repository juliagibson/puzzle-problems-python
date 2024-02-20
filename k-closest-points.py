# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
#
# Example 1: 
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
#
# Example 2:
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
#
# Leetcode accepted

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        kClosestPoints = []
        
        for point in points:
            dist = sqrt(point[0]**2 + point[1]**2)
            point.insert(0, dist)

        # sort by new distance entries in points entries
        points.sort(key = lambda row : row[0])

        for i in range(0, k):
            del points[i][0]
            kClosestPoints.append(points[i])
                    
        return kClosestPoints
