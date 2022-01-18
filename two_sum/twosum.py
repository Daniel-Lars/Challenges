# Sum of two: Given a list of integers and a target:
# return the list index of the 2 integers, that added up equals the target

nums = [1,3,3,4]
target = 6

for idx, a in enumerate(nums):
    for b in nums[idx + 1:]:
        if sum((a,b)) == target:
            if a != b:
                print([idx, nums.index(b)])
            else:
                print([idx, nums.index(b,idx+1)])
