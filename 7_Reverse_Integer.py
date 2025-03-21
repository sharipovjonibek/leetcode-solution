class Solution(object):
    def reverse(self, x):
        if x>0:
            y=str(x)
            k=int(y[::-1])
        else:
            x=abs(x)
            y=str(x)
            k=(-1)*int(y[::-1])
        if k>=(-2)**(31) and k<=(2**(31)-1):
            return k
        else:
            return 0