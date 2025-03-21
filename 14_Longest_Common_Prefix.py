class Solution(object):
    def longestCommonPrefix(self, strs):
        count=0
        min=10000
        str=""
        for element in strs:
            if len(element)<min:
                min=len(element)
                str=element
        for i in range(len(str)):
            for x in range(len(strs)):
                if strs[x][i]!=str[i]:
                    return str[0:count]
            count+=1
        return str[0:count]


                

                    
            
        