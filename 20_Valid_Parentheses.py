class Solution(object):
    def isValid(self, s):
        if s[0]!="(" and s[0]!="[" and s[0]!="{":
            return False
        else:
            mapping={")":"(","]":"[","}":"{"}
            stack=[]
            for item in s:
                if item in mapping:
                    top_element=stack.pop() if stack else "#"
                    if mapping[item]!=top_element:
                        return False
                else:
                    stack.append(item)
            return not stack


        

            


        