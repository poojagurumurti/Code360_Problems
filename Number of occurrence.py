# Problem statement
# Send feedback
# You have been given a sorted array/list of integers 'arr' of size 'n' and an integer 'x'.
# Find the total number of occurrences of 'x' in the array/list.
# Example:
# Input: 'n' = 7, 'x' = 3
# 'arr' = [1, 1, 1, 2, 2, 3, 3]

# Output: 2

# Explanation: Total occurrences of '3' in the array 'arr' is 2.


# Detailed explanation ( Input/output format, Notes, Images )
# Sample Input 1:
# 7 3
# 1 1 1 2 2 3 3


# Sample Output 1:
# 2


# Explanation For Sample Input 1:
# In the given list, there are 2 occurrences of integer 3.


# Sample Input 2:
#  5 6
#  1 2 4 4 5


# Sample Output 2:
#  0


# Explanation For Sample Input 2:
# In the given list, there are 0 occurrences of integer 6.


# Expected time complexity:
# The expected time complexity is O(log 'n').


# Constraints:
# 1 <= n <= 10^4
# 1 <= arr[i] <= 10^9
# 1 <= x <= 10^9
# Where arr[i] represents the element i-th element in the array/list.

# Time Limit: 1sec

from typing import List, Tuple

def lowerbound(arr: List[int], n: int, x: int) -> int:
    low, high = 0, n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def upperbound(arr: List[int], n: int, x: int) -> int:
    low, high = 0, n - 1
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > x:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def firstAndLastPosition(arr: List[int], n: int, k: int) -> Tuple[int, int]:
    lb = lowerbound(arr, n, k)
    if lb == n or arr[lb] != k:
        return (-1, -1)
    return (lb, upperbound(arr, n, k) - 1)


