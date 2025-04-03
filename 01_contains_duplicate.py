"""
01. Contains Duplicate
Given an integer array nums, return 'true' if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""

from typing import List


class Solution:
    '''
    This is brute approach to solve this question where we iterate over the list and check each element to every 
    other element present to the right. Whether the element we are checking and facing are the same are not.
    '''
    def hasDuplicateBruteForce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False
         

def main():
    # Creating an instance of class
    solution = Solution()
    result = solution.hasDuplicateBruteForce([1, 2, 3, 3])
    print(result)


if __name__ == "__main__":
    main()