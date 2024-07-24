'''
Alex and Chris are learning to infiltrate a secure system. Starting with a string of code,
Alex will remove any substring with an odd number of vowels. Chris then removes any substring from the remaining code with an even number of vowels.
This learning continues until one of them is unable to make a move. Given an array of strings of code,
determine the winner of each round and report the results as either "Alex" or "Chris" accordingly. Assume both act optimally.

Note: The vowels considered are a, e, i, o, and u.

Constraints:
    - 1 <= n <= 100
    - 1 <= [s[i]] <= 10^5
    - All strings consist of lowercase English letters only.

Example

Given n = 3 and s = ["iljs", "thr", "gns"]

    - In the 1st round, the whole string "iljs" contains 1 vowel (odd), so Alex chooses the whole string. Now the string is "" (empty string), and Chris cannot make a move, hence Alex wins the round.
    - In the 2nd round, the string "thr" does not contain any vowel hence Alex cannot make a move. Therefore Chris wins the round.
    - In the 3rd round, the string "gns" does not contain any vowel, so again Chris wins the round.

Hence, the aswer is ["Alex", "Chris", "Chris"]


UPI ->

Understand:
    - The winner will the user that is unable to make a move.
    - Alex removes odd number of vowels.
    - If there is no vowels contain in the string, Chris win.
    - Chris removes even number of vowels.

Plan:
    - To clarify code we can use helper functions
    - Function #1 counts the number of vowels in the string to help us determine if it contains even or odd number of vowels.


Implement

'''

def countVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for eachChar in s:
        if eachChar in vowels:
            count += 1
    return count

def getWho(s):
    winner = []
    for eachString in s:
        if countVowels(eachString) % 2 != 0 and countVowels(eachString) != 0:
            # If the string contains odd number of vowels
            winner.append("Alex")
        elif countVowels(eachString) % 2 == 0 and countVowels(eachString) != 0:
            # If the string contains even number of vowels
            winner.append("Chris")
        else:
            # If there is no vowel, Chris wins
            winner.append("Chris")
    return winner

# print(getWho(["iljs", "thr", "gns"]))
# print(getWho(['Igzpc', 'lchlo', 'xrwzg'] ))

edge_cases = [
    (["bcd", "fgh"], ["Chris", "Chris"]),
    (["aeiou", "aeae", "ioioi"], ["Alex", "Chris", "Alex"]),
    (["abcde", "xyzo", "pqrstuv", "abcdeu"], ["Alex", "Chris", "Alex", "Alex"]),
    (["a", "b", "e", "x"], ["Alex", "Chris", "Alex", "Chris"]),
    (["", ""], ["Chris", "Chris"]),
    (["a" * 100000, "b" * 99999 + "a"], ["Alex", "Alex"]),
]

for i, (test_case, expected) in enumerate(edge_cases):
    result = getWho(test_case)
    print(f"Test Case {i + 1}: {'Passed' if result == expected else 'Failed'}")