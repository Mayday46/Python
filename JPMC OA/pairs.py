'''

Consider two arrays of integers, a[n] and b[n]. What is the maximum number of pairs that can be formed where a[i] > b[i].
Each element can be in no more than one pair.

Find the maximum number of such possible pairs

Example:

    n = 3
    a = [1, 2, 3]
    b = [1, 2, 1]

Two ways the maximum number of paris can be selected.
    - (a[1], b[0]) = (2, 1) and (a[2], b[2]) = (3, 1) are valid pairs.
    - (a[1], b[0]) = (2, 1) and (a[2], b[1]) = (3, 2) are valid pairs.

No more then 2 pairs can be formed, so return 2.

UPI

Plan
    - Sorted list a in decending way
    - [3, 2, 1, 1]
    - [1, 1, 2, 0]

'''

def findNumOfPairs(a, b):
    a.sort(reverse = True)
    b.sort()
    upper, lower, count = 0, 0, 0

    while upper < len(a) and lower < len(b):
        if a[upper] > b[lower]:
            count += 1
            upper += 1
            lower += 1
        else:
            upper += 1
    return count
# Example usage


a = [1, 2, 3, 4, 5]
b = [6, 6, 1, 1, 1]

print(findNumOfPairs(a, b))  # Expected output: 1



