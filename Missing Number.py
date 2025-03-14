# Missing Number
# Problem statement
# Send feedback
# Given an array ‘a’ of size ‘n’-1 with elements of range 1 to ‘n’. The array does not contain any duplicates. Your task is to find the missing number.

# For example:
# Input:
# 'a' = [1, 2, 4, 5], 'n' = 5

# Output :
# 3

# Explanation: 3 is the missing value in the range 1 to 5.
# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1 :
# 4 
# 1 2 3
# Sample Output 1:
# 4
# Explanation Of Sample Input 1:
# 4 is the missing value in the range 1 to 4.
# Sample Input 2:
# 8
# 1 2 3 5 6 7 8
# Sample Output 2:
# 4
# Explanation Of Sample Input 2:
# 4 is the missing value in the range 1 to 8.
# Expected time complexity:
# The expected time complexity is O(n).
# Constraints:
# 1 <= 'n' <= 10^6 
# 1 <= 'a'[i] <= 'n'
# Time Limit: 1 sec


from typing import *

def missingNumber(a : List[int], N : int) -> int:
    # Write your code here.
    summation = (N * (N + 1)) // 2
    s2 = sum(a)
    differ = summation - s2
    return differ


