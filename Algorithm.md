# Given:
Input line 1: a list of space separated strings (names)
Input line 2: an integer, m

# Task:

Generate the max number of randomized groups with up to m names per group, with no group having more than 1 less member than any other group


# Algorithm:

Check if the number of names is perfectly divisible by the max number of people per group. If so, generate # of names/m lists (groups).
If not, generate (# of names/m) + 1 lists (I have no idea why I decided to make a group object with a names parameter that is just a list).

Iterate over each group, assigning randomly selected people and removing them from the list of options until the list of people is empty.
