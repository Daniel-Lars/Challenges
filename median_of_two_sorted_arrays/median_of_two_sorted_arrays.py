import math

nums1 = []
nums2 = [1,2,3,4,5]

nums1.extend(nums2)
nums1.sort()
res = None
print(len(nums1) % 2)
if len(nums1) % 2 != 0:
    indicator = int(math.ceil(len(nums1) / 2))
    print(indicator)
    res = nums1[indicator-1]
else:
    indicator = int(len(nums1)/2)
    list_lower_half = nums1[:indicator]
    list_upper_half = nums1[indicator:]
    res = (list_lower_half[-1] + list_upper_half[0])/2

print(res)
