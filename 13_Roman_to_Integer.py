class Solution(object):
    def romanToInt(self, s):
        answer=0
        if "IV" in s or "IX" in s or "XL" in s or "XC" in s or "CD" in s or "CM" in s:
            s=s.replace("IV","R")
            s=s.replace("IX","E")
            s=s.replace("XL","K")
            s=s.replace("XC","P")
            s=s.replace("CD","U")
            s=s.replace("CM","Y")
            
        
        for element in s:
            if element=="R":
                answer+=4
            elif element=="E":
                answer+=9
            elif element=="K":
                answer+=40
            elif element=="P":
                answer+=90
            elif element=="U":
                answer+=400
            elif element=="Y":
                answer+=900
            elif element=="I":
                answer+=1
            elif element=="V":
                answer+=5
            elif element=="X":
                answer+=10
            elif element=="L":
                answer+=50
            elif element=="C":
                answer+=100
            elif element=="D":
                answer+=500
            elif element=="M":
                answer+=1000
        return answer