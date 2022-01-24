class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x:x[0])
        minumum = -10000
        maximum = -10000
        m=[]
        for i in range(len(intervals)):
            if(intervals[i][0]>maximum):
                if(i!=0):
                    m.append([minimum,maximum])
                minimum = intervals[i][0]
                maximum = intervals[i][1]
            else:
                if(intervals[i][1]>maximum):
                    maximum = intervals[i][1]
        if(maximum!=-10000 and [minimum,maximum] not in m):
            m.append([minimum,maximum])
        return m