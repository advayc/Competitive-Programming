class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL",10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        total=''
        for key, value in romans.items():
            while num>=key:
                total+= value
                num -= key
        return total