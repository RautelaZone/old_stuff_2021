"""
1) Generators are a simple way of creating iterators.
2) A generator-function is defined like a normal function, but whenever
it needs to generate a value, it does so with the yield keyword rather than return.
3) Any function that contains a yield keyword is termed as Generator.

Below is the generator to yield n^2 for each element in the given list
"""

nums = [1, 2, 3, 4, 5]

def gen_fun(nums):
    for n in nums:
        yield n * n

my_gen = gen_fun(nums)

for i in my_gen:
    print(i)
