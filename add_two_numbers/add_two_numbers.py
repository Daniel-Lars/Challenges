# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.

l1 = [2, 4, 3]
l2 = [5, 6, 4]

# Reverse the given lists
l1_reversed = l1[::-1]
l2_reversed = l2[::-1]

# Convert items to string to join
l1_reversed = [str(i) for i in l1_reversed]
l2_reversed = [str(i) for i in l2_reversed]

# Create reversed number and add the numbers together
res_l1 = int("".join(l1_reversed))
res_l2 = int("".join(l2_reversed))
new_num = str(res_l1 + res_l2)

# Create list of digits of the new number
final_list = []
for i in new_num:
    final_list.append(i)

print(final_list)
