from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[1])
        
        size = 0
        prev_points = [] 
        
        for curr_start, curr_end in intervals:
           
            if len(prev_points) < 2 or prev_points[-2] < curr_start:
                
                prev_points.append(curr_end - 1)
                prev_points.append(curr_end)
                size += 2
            elif prev_points[-1] < curr_start:
                
                prev_points.append(curr_end)
                size += 1

        return size
