# Daily Coding Practice 02.03.2025

""" Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass? """

def two_sums(nums, k):
    for num in nums:
        complement = k - num
        if complement in nums:
            return True
        else:
            return False

print(two_sums([10, 15, 3, 7], 17))