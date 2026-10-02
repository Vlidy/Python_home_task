class Solution:
    def minMeetingRooms(self, start, end):
        masst=sorted(start)
        massend=sorted(end)
        endp=0
        rooms=0
        for x in masst:
            if x<massend[endp]:
                rooms+=1
            else:
                endp+=1
        return rooms
        
# solution to the original tasks (is not evalibale on leetcode)
# from typing import (
#     List,
# )
# from lintcode import (
#     Interval,
# )

# """
# Definition of Interval:
# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
# """

# class Solution:
#     """
#     @param intervals: an array of meeting time intervals
#     @return: the minimum number of conference rooms required
#     """
#     def min_meeting_rooms(self, intervals: List[Interval]) -> int:
#         masst=[]
#         massend=[]
#         for x in intervals:
#             masst.append(x.start)
#             massend.append(x.end)
#         masst=sorted(masst)
#         massend=sorted(massend)
#         endp=0
#         rooms=0
#         for x in masst:
#             if x<massend[endp]:
#                 room+=1
#             else:
#                 endp+=1
#         return room
