import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# Runtime of 7.15
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# with open('output.txt', 'w') as f_out:
#     for dupes in duplicates:
#         print('\n', dupes, end="", file=f_out)

# Optimized to O(n log n) with binary search
# Runtime of 0.129

# binary_search = BSTNode(names_1[0])

# for names in names_1:
#     if names != names_1[0]:
#         binary_search.insert(names)

# for names in names_2:
#     if binary_search.contains(names):
#         duplicates.append(names)

# with open('output_optimized.txt', 'w') as f_out:
#     for dupes in duplicates:
#         print('\n', dupes, end="", file=f_out)

# f_out.close()

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# Runtime of 0.006
# O(n)

# names_dict = {}  # Dictionary

# for names in names_1:
#     names_dict[names] = names

# for names in names_2:
#     if names in names_dict:
#         duplicates.append(names)

# with open('output_optimized_stretch.txt', 'w') as f_out:
#     for dupes in duplicates:
#         print('\n', dupes, end="", file=f_out)

# f_out.close()


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
