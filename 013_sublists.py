"""
Make a solution that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists. Items of the same value should be in the same sublist.

Examples [2, 1, 2, 1] ➞ [[2, 2], [1, 1]], [5, 4, 5, 5, 4, 3] ➞ [[5, 5, 5], [4, 4], [3]], ["b", "a", "b", "a", "c"] ➞ [["b", "b"], ["a", "a"], ["c"]]
Notes The sublists should be returned in the order of each element's first appearance in the given list.
"""

liste = [5, 4, 5, 5, 4, 3]
repeat = {}
for i in liste:
    if i not in repeat:
        repeat[i] = [i]
    else:
        repeat[i] += [i]

print(list(repeat.values()))
