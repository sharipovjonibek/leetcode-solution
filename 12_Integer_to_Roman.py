class Solution(object):
    def intToRoman(self, num):
        roman_number=""
        roman_1 = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"}
        roman_10 = {10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC"}
        roman_100 = {100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM"}
        roman_1000 = {1000: "M", 2000: "MM", 3000: "MMM"}
        y=str(num)
        length=len(y)
        if length==1:
            roman_number+=roman_1[num]
        elif length==2:
            roman_number+=roman_10[int(y[0])*10]
            if y[1]!="0":
                roman_number+=roman_1[int(y[1])]
        elif length==3:
            roman_number+=roman_100[int(y[0])*100]
            if y[1]!="0":
                roman_number+=roman_10[int(y[1])*10]
            if y[2]!="0":
                roman_number+=roman_1[int(y[2])]
        elif length==4:
            roman_number+=roman_1000[int(y[0])*1000]
            if y[1]!="0":
                roman_number+=roman_100[int(y[1])*100]
            if y[2]!="0":
                roman_number+=roman_10[int(y[2])*10]
            if y[3]!="0":
                roman_number+=roman_1[int(y[3])]
        return roman_number