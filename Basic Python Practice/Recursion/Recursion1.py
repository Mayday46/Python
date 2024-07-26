def is_nested(paren_s):
    # Base cases
    if paren_s == "":
        return True
    if paren_s == "()":
        return True
    
    # Recursive case
    if paren_s[0] == '(' and paren_s[-1] == ')':
        return is_nested(paren_s[1:-1])
    else:
        return False


def count_ones(lsts):
    if not lsts:
        # If the list is empty
        return 0 
    return (1 if lsts[0] == 1 else 0) + count_ones(lsts[1:])

def binarySearch(lsts, target):
    left, right = 0, len(lsts) - 1
    while left <= right:
        middle = (left + right) // 2
        if lsts[middle] < target:
            # Meaning that the current middle value is smaller than the target
            # The target will be on the right side.
            # Discard left side of the list
            left = middle + 1
        elif lsts[middle] > target:
            right = middle - 1
        else:
            return middle
    return f"{target} not exist within the list.."

def binarySearch_Recursion(lsts, target, left=0, right=None):
    if right is None:
        right = len(lsts) - 1
        
    if left > right:
        return f"{target} not exist within the list.."
    
    middle = (left + right) // 2
    
    if lsts[middle] == target:
        return middle
    elif lsts[middle] < target:
        # The target will be on the right side, discard the left side of the list
        return binarySearch_Recursion(lsts, target, middle + 1, right)
    else:
        # The target will be on the left side, discard the right side of the list
        return binarySearch_Recursion(lsts, target, left, middle - 1)


# lsts = [0, 0, 0, 0, 1, 1, 1]
# print(count_ones(lsts))

# Example Usage
# print(is_nested("((()))"))  # Expected Output: True
# print(is_nested("(()"))     # Expected Output: False
# print(is_nested("()()"))    # Expected Output: False
# print(is_nested("(())"))    # Expected Output: True

binaryList = [1, 2, 34, 46, 2000, 123, 555]
print(binarySearch(binaryList, 555))
print(binarySearch_Recursion(binaryList, 555))
