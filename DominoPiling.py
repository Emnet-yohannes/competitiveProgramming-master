import math
def dominoPiling(n,m):
    #print(math.floor((n*m)/2))
    return math.floor((n*m)/2)

n,m = list(map(int, input().split()))
print(dominoPiling(n,m))
#dominoPiling(3,3)