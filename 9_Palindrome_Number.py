class Solution(object):
    def isPalindrome(self, x):
        if x>=0:
            x=str(x)
            y=x[::-1]
            if x==y:
                return True
            else:
                return False
        else:
            return False


        