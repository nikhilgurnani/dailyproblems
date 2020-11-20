"""
You are given a string s, and an integer k. Return the length of the longest substring in s that contains at most k distinct characters.

For instance, given the string:
aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.

aabcdefff

i = a
[a]
count = 1

i = a
[a]
count = 2

i = b
[a, b]
count = 3

i = c
[a, b, c]
count = 4

i = d


"""


def longest_substring_with_k_distinct_characters(s, k):
    unique_elements = set()
    max_length = 0

    current_count = 0
    for i in s:
        if i in unique_elements:
            current_count += 1
        else:
            if len(unique_elements) == k:
                current_count = 1
                unique_elements.clear()
                unique_elements.add(i)
            else:
                unique_elements.add(i)
                current_count += 1

        max_length = max(current_count, max_length)
    return max_length


print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
print(longest_substring_with_k_distinct_characters('aabbcc', 3))
print(longest_substring_with_k_distinct_characters('aabbcc', 2))
