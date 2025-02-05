"""Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?"""

# With division
def product_except_self(nums):
    total_product = 1
    zero_count = 0
    for num in nums:
        if num != 0:
            total_product *= num
        else:
            zero_count += 1
    
    result = []

    for num in nums:
        if zero_count > 1:
            result.append(0)
        elif zero_count == 1:
            result.append(0 if num != 0 else total_product)
        else:
            result.append(total_product // num)
    return result

print(product_except_self([1, 2, 3, 4, 5]))
print(product_except_self([3, 2, 1]))

# Without division

def product_except_self(nums):
    n = len(nums)
    result = [1] * n

    left_product = 1
    for i in range(n):
        result[i] = left_product
        left_product *= nums[i]
   

    right_product = 1
    for i in range(n-1, -1, -1):
        result[i] = result[i] * right_product
        right_product *= nums[i]
    return result

print(product_except_self([1, 2, 3, 4, 5]))
print(product_except_self([3, 2, 1]))
