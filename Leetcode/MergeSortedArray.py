'''

Top Interview 150

88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integer
m and n, representing the number of elements in nums1 and num2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums12 has a length of m + n, where the first m elements denoted the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n

Example 1:
    - Input: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3
    - Output: [1, 2, 2, 3, 5, 6]
    - Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6] with the underlined
        elements coming from nums1.



UPI

Understand:
    - Two given array are sorted.
    - Output needs to be ascending order.
    - Need to modify it on the spot.
    - Returning nums1 after modification.
    - Assume that there might be duplicates within the list.
    - m and n are the element that we are merging.
    - Ouput nums1 will have a size of m + n.
    - Since nums1 will have a size of (m + n), meaning that there is only element of nums1 that we need to modify.

Plan:
    - Two pointer method, comparing each element at the same time.
    - Start from the end of m and n [the real value we are comparing] moving forward.
    - Have a pointer from the very end of the list nums1. To store the larger element.

Implement:
    - 


'''


'''
    pointer1
       |
       v
[1, 2, 3, 0, 0, 0]
                ^
                |
                endPointer

[2, 5, 6]
       ^
       |
       pointer2
'''


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:

    endPointer = (m + n) - 1 # Or simply len(nums1) - 1
    pointer1 = m - 1 # Pointed to the actual last element we're comparing in nums1
    pointer2 = n - 1 # Pointed to the actual last element we're comparing in nums2

    while pointer1 >= 0 and pointer2 >= 0:

        if nums1[pointer1] > nums2[pointer2]: # If the current value in nums1 is bigger than the current value in nums2
            nums1[endPointer] = nums1[pointer1]
            pointer1 -= 1
        else: # Else that the nums1[pointer1] < nums2[pointer2].
            # If we found a larger element, then we stored them in the end.
            nums1[endPointer] = nums2[pointer2]
            pointer2 -= 1
        endPointer -= 1
    

    '''
    nums1: [1, 2, 3, 0, 0, 6]  # pointer2 = 2 -> 1
    nums1: [1, 2, 3, 0, 5, 6]  # pointer2 = 1 -> 0
    nums1: [1, 2, 3, 3, 5, 6]  # pointer1 = 2 -> 1
    nums1: [1, 2, 2, 3, 5, 6]  # pointer2 = 0 -> -1
    
    '''
    while pointer2 >= 0:
        # If there is any left over element in nums2
        nums1[endPointer] = nums2[pointer2]
        pointer2 -= 1
        endPointer -= 1



a = [1, 2, 3, 0, 0, 0]
b = [2, 5, 6]
print(a)
print(b)
merge(nums1=a, m = 3, nums2=b, n = 3)
print(a)


