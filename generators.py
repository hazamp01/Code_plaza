# without generator
def square_num(nums):
    result = []
    for num in nums:
        result.append(num * num)
    return result


mynums = square_num([1, 2, 3, 4, 5])
print mynums


# with yield generator

def sqr_num(nums):
    for num in nums:
        yield num * num


num = sqr_num([1, 2, 3, 4, 5, 6])
for i in num:
    print i
