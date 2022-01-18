# Sum of two: Given a list of integers and a target:
# return the list index of the 2 integers, that added up equals the target

nums = [3, 2, 4]
target = 6


for i in nums:
    check = target - i
    try:
        if check in nums:
            print(nums.index(i), nums.index(check,nums.index(i)+1))
            break
    except ValueError:
        pass
