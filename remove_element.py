from typing import List


class Solution:

    def remove_element(
            self,
            nums: List[int],
            val: int
    ) -> int:
        if not nums:
            return 0

        k, i = 0, 0

        while i < len(nums):

            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            i += 1

        # return k
        print(k)


def res():
    inputs = (
        (
            [3, 2, 2, 3],
            3s
        ),
        (
            [0, 1, 2, 2, 3, 0, 4, 2],
            2
        ),
    )
    test = Solution()

    for nums, val in inputs:
        test.remove_element(nums, val)
        print('----')


if __name__ == '__main__':
    res()

# Сложность алгоритма по времени: О(n)
# Сложность алгоритма по памяти: О(2)
