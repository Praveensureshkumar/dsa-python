class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[]
        staring=intervals[0][0]
        ending=intervals[0][-1]
        for i in range(1,len(intervals)):
            if staring<=intervals[i][0]<=ending:
                if intervals[i][-1]>ending:
                    ending=intervals[i][-1]
            else:
                result.append([staring,ending])
                staring=intervals[i][0]
                ending=intervals[i][-1]
        result.append([staring,ending])        
        return result