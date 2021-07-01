class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = str(n)
        product = 1
        sum1 = 0
        for y in range(0,len(x)):
            o = ord(x[y])-48
            product = product *o
            sum1= sum1 + (ord(x[y])-48)
        return product-sum1