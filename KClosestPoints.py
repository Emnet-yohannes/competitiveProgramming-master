class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceArray=[]
        for i in range(len(points)):
            d=sqrt(pow(points[i][0],2)+pow(points[i][1],2))
            distanceArray.append(d)
        minArray=[]
        for j in range(k):
                mini = min(distanceArray)
                minArray.append(points[distanceArray.index(mini)])
                del points[distanceArray.index(mini)]
                del distanceArray[distanceArray.index(mini)]
        return minArray