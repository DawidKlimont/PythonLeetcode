from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)<=len(nums2):
            shorter = nums1
            longer = nums2
        else:
            shorter = nums2
            longer = nums1

        total_len = len(nums1)+len(nums2)
        is_total_len_uneven = total_len%2
        total_len_half = total_len//2

        lower = 0
        higher = len(shorter)

        while True:
            pivot_shorter = lower + (higher-lower)//2
            pivot_longer = total_len_half - pivot_shorter

            if pivot_shorter-1 >= 0:
                left_shorter = shorter[pivot_shorter-1]
            else:
                left_shorter = float('-inf')
            if pivot_shorter < len(shorter):
                right_shorter = shorter[pivot_shorter]
            else:
                right_shorter = float('inf')

            if pivot_longer-1 >= 0:
                left_longer = longer[pivot_longer-1]
            else:
                left_longer = float('-inf')
            if pivot_longer < len(longer):
                right_longer = longer[pivot_longer]
            else:
                right_longer = float('inf')
            if left_shorter <= right_longer and left_longer <= right_shorter:
                if is_total_len_uneven:
                    return min(right_longer,right_shorter)
                else:
                    return (max(left_longer,left_shorter) + min(right_longer,right_shorter))/2
            elif left_shorter > right_longer:
                higher = pivot_shorter-1
            elif right_shorter < left_longer:
                lower = pivot_shorter+1
