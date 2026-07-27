"""
Problem: 496. Next Greater Element I
Difficulty: Easy
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for i in nums1:
            j = nums2.index(i)
            found = -1
            for k in range(j + 1, len(nums2)):
                if nums2[k] > i:
                    found = nums2[k]
                    break
            l.append(found)
        return l
