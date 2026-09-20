# Problem: Roman to Integer
# Difficulty: Easy

class Solution(object):
    def romanToInt(self, s):
        roman_dict = {
          "I": 1,
          "V": 5,
          "X": 10,
          "L": 50,
          "C": 100,
          "D": 500,
          "M": 1000
        }
        integer = 0
        roman_list = [char for char in s]
        for index, char in enumerate(roman_list, start=1):
            if index < len(roman_list):
                if roman_dict[char] >= roman_dict[roman_list[index]]:
                    integer += roman_dict[char]
                elif roman_dict[char] < roman_dict[roman_list[index]]:
                    integer -= roman_dict[char]
                else:
                    return "Invalid Roman Value!"
            elif index == len(roman_list):
                integer += roman_dict[char]
        return integer