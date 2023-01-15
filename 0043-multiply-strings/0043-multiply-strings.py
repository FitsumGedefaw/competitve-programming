class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dict = {"0": 0,"1":1 ,"2":2 ,"3": 3,"4": 4,"5":5 ,"6": 6,"7": 7,"8":8,"9":9 }
        xlen = len(num1)
        ylen = len(num2)
        x =y =0
        for i,n in enumerate(num1):
            x += (10**(xlen - (i+1)) * dict[n])
        for i,n in enumerate(num2):
            y += (10**(ylen - (i+1)) * dict[n])
        return str(x * y)