nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
nums.sort()

start = 0
end = len(nums) - 1

while start < end:
    if nums[start] == nums[start + 1]:
        nums.pop(start)
        end -= 1
        start -= 1
    start += 1

print("Length:", start)
print("Array without duplicate values:", nums)
