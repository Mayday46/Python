'''
1356. Sort Integers by The Number of 1 Bits

You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation
and in case of two or more integers have the same number of 1's you have to sort them in ascending order.
Return the array after sorting it.

Example 1:
    - Input: arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    - Output: [0, 1, 2, 4, 8, 3, 5, 6, 7]
    - Explanation: [0] is the only integer with 0 bits.
        - [1, 2, 4, 8] all have 1 bit
        - [3, 5, 6] have 2 bits
        - [7] has 3 bits
        - The sorted array by bits is [0, 1, 2, 4, 8, 3, 5, 6, 7]

Example 2:
    - Input: arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    - Output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    - Explanation: All integer has 1 bit in binary representation, you should just sort them in ascending order.

UPI
    Understand:
        - Convert integer in array to binary.
        - Sort integer based on their binary form.

    Plan:
        - Find a way to convert each integer into binary form.
            - This binary conversion function, should not only convert but also checks the number of 1 that this integer contains.
        - Find a way to sort the integer based on their binary form.

    Implement:

'''

def binaryConverter(number):
    binaryForms = bin(number)[2:]
    return binaryForms

def bitCounter(binary):
    return binary.count('1')


def sortByBits(arr: list[int]) -> list[int]:
    reference = dict()
    result = []
    
    for each in arr:
        currentConversion = binaryConverter(each)
        bit_counter = bitCounter(currentConversion)

        if bit_counter not in reference:
            reference[bit_counter] = [each]
        else:
            reference[bit_counter].append(each)
    
    for key in sorted(reference.keys()):
        sorted_values = sorted(reference[key])
        result.extend(sorted_values)
    return result

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(sortByBits(arr))




# for i in range(11):
#     print(f"{i} -> {binaryConverter(i)}")