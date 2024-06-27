
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            # If the number has a divisor... then it is not prime.
            return False
    return True

# print(is_prime(5))
# print(is_prime(12))
# print(is_prime(9))


# Write a function that reverse any list.

def reverse_list(lst):
    newlst = []
    for i in range(len(lst) - 1, -1, -1):
        newlst.append(lst[i])
    return newlst
    # Run time -> O(n)
        # Pointer from start from the end. Linear time, the bigger the size the longer it take for it to iterate.
    # Space Complexity -> O(n)
        # It creates a new list which depended on the size of the input list. The bigger of the input list the bigger then output list.

# print(reverse_list([1, 2, 3, 4, 5]))

def reverse_list2(lst):
    # Two pointer method
    pointer1 = 0
    pointer2 = len(lst) - 1

    while pointer1 < pointer2:
        lst[pointer1], lst[pointer2] = lst[pointer2], lst[pointer1]
        pointer1 += 1
        pointer2 -= 1
    return lst
    # Run time -> O(n/2)
        # Two pointers are used, one from the beginning and one from end. Cutting the linear runtime in half.
    # Space Complexity -> O(1)
        # Constant time, there is no extra space utilized as previous method. Swap are done right on the spot.

# print(reverse_list2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

def sort_array_by_parity(nums):
    evenlist = []
    oddlist = []

    for each in nums:
        if each % 2 == 0:
            evenlist.append(each)
        else:
            oddlist.append(each)
    return evenlist + oddlist

nums = [3,1,2,4]
nums2 = [0]
# print(sort_array_by_parity(nums))
# print(sort_array_by_parity(nums2))


def is_palindrome(word): # -> Helper function
    pointer1 = 0
    pointer2 = len(word) - 1
    
    while pointer1 < pointer2:
        if word[pointer1] == word[pointer2]:
            pointer1 += 1
            pointer2 -= 1
        else:
            return False
    return True
# print(is_palindrome("ada"))
# print(is_palindrome("cool"))
# print(is_palindrome("ooo"))
# print(is_palindrome("car"))

def first_palindrome(words):
    plaindrome = ""
    for word in words:
        if is_palindrome(word):
            plaindrome = word
            break
    return plaindrome

# words = ["abc","car","ada","racecar","cool"]
# palindrome1 = first_palindrome(words)
# print(palindrome1)

# words2 = ["abc","racecar","cool"]
# palindrome2 = first_palindrome(words2)
# print(palindrome2)

# words3 = ["abc", "def", "ghi"]
# palindrome3 = first_palindrome(words3)
# print(palindrome3)

def remove_duplicates(nums):
    
    i = 0  # Set the initial pointer for comparison
    while i < len(nums) - 1:  # Loop until the second to last element
        if nums[i] == nums[i + 1]:  # Check if current and next elements are the same
            del nums[i]  # Remove the current element
        else:
            i += 1  # Move to the next element only if no deletion occurs

def remove_duplicates2(nums):
    
    last_unique_index = 0  # Initialize a pointer for the last unique element's index

    # Iterate over the array starting from the second element
    for i in range(1, len(nums)):
        if nums[i] != nums[last_unique_index]:
            last_unique_index += 1
            nums[last_unique_index] = nums[i]

    # Use slicing to modify the original list to contain only unique elements
    nums[:] = nums[:last_unique_index + 1]

    return last_unique_index + 1

# Example usage
nums = [1, 1, 2, 3, 4, 4, 4, 5]
print("Original list:", nums)
new_length = remove_duplicates(nums)
print("New length after removing duplicates:", new_length)
print("List after duplicates removed:", nums)



# nums = [1,1,2,3,4,4,4,5]
# print(nums)
# print(remove_duplicates(nums))
# print(nums) # same list

def is_long_pressed(name, typed):
    return len(set(typed)) == len(name)

# name = "alex"
# typed = "aaleex"
# print(is_long_pressed(name, typed))

# name2 = "saeed"
# typed2 = "ssaaedd"
# print(is_long_pressed(name2, typed2))

# name3 = "courtney"
# typed3 = "courtney"
# print(is_long_pressed(name3, typed3))

def test(number):
    reference = dict()
    for i in range(1, number + 1):
        reference[i] = i * i
    return reference

# print(test(5))

def squish(x):
    res = []
    val = x[0]
    count = 1
    for i in range(1, len(x)):
        if x[i] == val: # Repeated
            count += 1
        else:
            res.append((val, count))
            count = 1
            val = x[i]
    res.append((val, count))
    return res

print(squish([4, 4, 4, 6, 6, 8, 8, 8, 8]))

from itertools import groupby
def squish2(x):
    return [(key, len(list(group))) for key, group in groupby(x)]

