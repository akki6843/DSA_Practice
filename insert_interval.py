"""
You are given an array of non-overlapping intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Sample Input
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
Sample Output
[[1,2],[3,10],[12,16]]
Explanation
Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 10^4

nintervals[i].length == 2

0 <= starti <= endi <= 10^5

intervals is sorted by starti in ascending order.

newInterval.length == 2

0 <= start <= end <= 10^5
"""