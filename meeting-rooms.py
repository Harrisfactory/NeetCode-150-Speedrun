from operator import itemgetter

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        if len(intervals) == 0:
            return True

        #sorting by starting interval might work, we could then cycle through and compare first,last with next first last

        intervals = sorted(intervals, key=itemgetter(0))

        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        
        return True

        #O(nlog(n))