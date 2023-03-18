nums = [0,1,2,2,3,0,4,2]
val = 2
start = 0
end = len(nums)

while val in nums:
    nums.remove(val)
print("Length:", len(nums))
print(f"Array after removing {val}:", nums)