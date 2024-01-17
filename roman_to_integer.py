class Solution:

    def roman_to_int(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                total += roman_to_int[s[i]]

        # return total
        print(total)


def res():
    inputs = [
        'III',
        'LVIII',
        'MCMXCIV',
    ]

    test = Solution()

    for elem in inputs:
        test.roman_to_int(s=elem)
        print('----')


if __name__ == '__main__':
    res()

# Сложность алгоритма по времени: О(n)
# Сложность алгоритма по памяти: О(n)
