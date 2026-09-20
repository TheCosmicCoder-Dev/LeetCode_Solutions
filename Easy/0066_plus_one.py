# Problem: Plus One
# Difficulty: Easy

class Solution(object):
    def plusOne(self, digits):
        new_list = []

        for digit in digits:
            new_list.append(str(digit))

        num = int("".join(new_list))
        final_num = num + 1

        list1 = [int(char) for char in str(final_num)]
        return list1