class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number_str = "".join(map(str, digits))
        num_plus_one = str(int(number_str) + 1)
        result = [int(digit) for digit in num_plus_one]
        return result

# O(n)
