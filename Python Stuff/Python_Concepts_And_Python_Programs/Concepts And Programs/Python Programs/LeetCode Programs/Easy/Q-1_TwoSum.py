"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
"""

nums = [3, 2, 4]
target = 6


# Using for loop:
def indices(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(indices(nums, target))


# Using Dictionary:
# def twoSum(nums, target):
#     dictionary = {}
#     answer = []
#     for i in range(len(nums)):
#         secondNumber = target - nums[i]
#         if secondNumber in dictionary.keys():
#             secondIndex = nums.index(secondNumber)
#             if i != secondIndex:
#                 return sorted([i, secondIndex])
#         dictionary.update({nums[i]: i})
#
#
# print(twoSum(nums, target))
