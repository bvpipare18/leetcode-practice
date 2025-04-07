"""
01. Contains Duplicate
Given an integer array nums, return 'true' if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

Expected TC & SC:
TC - O(n)
SC - O(n)

where n is the size of the input array.
"""

from typing import List


class Solution:
    '''
    This is brute approach to solve this question where we iterate over the list and check each element to every 
    other element present to the right. Whether the element we are checking and facing are the same are not.

    TC - O(n^2)
    SC - O(1)
    '''
    def hasDuplicateBruteForce(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                
        return False


    '''
    This is better apporach than brute force apporach where we use a inbuilt sort() function to sort the array & check
    if any adajacent values are same or not.

    Read here - https://www.w3schools.com/python/ref_list_sort.asp

    TC - O(nlogn) 
    SC - O(1)/O(n) depending on the sorting algorithm
    '''
    def hasDuplicateSorting(self, nums:List[int]) -> bool:
        nums.sort() # Uses a Timsort and sorts a list in place
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True

        return False


    '''
    This is a better solution than a above sorting solution where we will use set data structure where it stores unique values.

    TC - O(n)
    SC - O(n)
    '''
    def hasDuplicateSet(self, nums:List[int]) -> bool:
        seenElements = set()
        for num in nums:
            if num in seenElements:
                return True
            seenElements.add(num)
        return False

    '''
    This is a solution that uses len() function where it calculates 
    TC - O(n)
    SC - O(n)
    '''
    def hasDuplicateSetLength(self, nums:List[int]) -> bool:
        return len(set(nums)) < len(nums)


def main():
    # Creating an instance of class
    solution = Solution()
    bruteForceResult = solution.hasDuplicateBruteForce([1, 2, 3, 3])
    print(bruteForceResult)

    sortingResult = solution.hasDuplicateSorting([1,2,3,3])
    print(sortingResult)

    setResult = solution.hasDuplicateSet([1,2,3,3])
    print(setResult)

    setResultLen = solution.hasDuplicateSetLength([1,2,3,3])
    print(setResultLen)


if __name__ == "__main__":
    main()