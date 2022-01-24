import math
def TheaterSquare(n,m,a):
    #print(math.floor((n*m)/2))
    if(n%a==0):
        d1=n//a
    else:
        d1 = n//a +1
    if(m%a==0):
        d2 = m // a
    else :
        d2 = m //a +1
    print(d1*d2)
    

n,m,a= list(map(int, input().split()))
# print(TheaterSquare(n,m,a))
# TheaterSquare(6,6,4)