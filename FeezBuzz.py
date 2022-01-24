from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        myList = []
        for x in range(1,n+1):
            if x % 5 ==0 and x % 3==0:
                myList.append("FizzBuzz")
            elif x % 3 == 0 :
                myList.append("Fizz")
            elif x % 5 == 0 :
                myList.append("Buzz")
            else:
                myList.append(str(x))
        print(myList)
        return myList 

"""myclass = Solution();
myclass.fizzBuzz(n=15)"""