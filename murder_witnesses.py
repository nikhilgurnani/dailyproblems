"""
There are n people lined up, and each have a height represented as an integer. A murder has happened right in front of them, and only people who are taller than everyone in front of them are able to see what has happened. How many witnesses are there?

Example:
Input: [3, 6, 3, 4, 1]
Output: 3
Explanation: Only [6, 4, 1] were able to see in front of them.
 #
 #
 # #
####
####
#####
36341                                 x (murder scene)

Key takeoffs:
* last element will always witness the crime scene
* max element will always witness the crime scene

Use stack
element > top_stack => top_stack cannot witness murder, so pop() and push(element)
"""

def witnesses(heights):
    witness = []
    stk = []

    witness.append( heights [ len( heights ) - 1 ] )

    i = 1
    stk.append( heights[0] )
    while i <= len( heights ) - 2:
        if stk[len(stk) - 1 ] <= heights[i]:
            stk.pop()
            stk.append(heights[i])
        else:
            stk.append(heights[i])

        i += 1

    stk = list(element for element in stk if element > witness[0])
    return stk + witness

print(witnesses([3, 6, 3, 4, 1])) # 3

print(witnesses([3, 3, 3, 4, 1])) # 2

print(witnesses([1, 2, 3, 4, 5, 6])) # 1

print(witnesses([6, 5, 4, 3, 2, 1])) # 6

print(witnesses([3, 6, 3, 4, 5])) # 2