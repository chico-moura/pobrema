def solution(nums: [int], odd: bool) -> [int]:
    return [num for num in nums if num % 2 == odd]


def par(nums: [int]) -> [int]:
    return solution(nums, odd=False)


def impar(nums: [int]) -> [int]:
    return solution(nums, odd=True)
