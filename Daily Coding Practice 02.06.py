"""Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""


def lowest_positive_integer(input):
    n = len(input)
    for i in range(n):
        while 1 <= input[i] <= n and input[i] != input[input[i] - 1]:
            input[input[i] - 1], input[i] = input[i], input[input[i] - 1]


    for i in range(n):
        if input[i] != i + 1:
            return i + 1

    return n + 1

# Test Case
print(lowest_positive_integer([3, 4, -1, 1]))
print(lowest_positive_integer([1, 2, 0]))