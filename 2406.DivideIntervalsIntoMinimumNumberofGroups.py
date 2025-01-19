from typing import List
from collections import defaultdict

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = defaultdict(int)
        
    
        for start, end in intervals:
            events[start] += 1  
            events[end + 1] -= 1  
        
       
        max_groups = 0
        current_groups = 0
        for time in sorted(events.keys()):
            current_groups += events[time]
            max_groups = max(max_groups, current_groups)
        
        return max_groups
