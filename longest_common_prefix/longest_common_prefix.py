# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


# example of strings - strs = ["flight", "flow", "fur"]

def longest_common_prefix(strs):
    # identify shortest string in list = max common prefix
    common_prefix = min(strs, key=len)
    # as long as prefix is >= 1 loop through the list and check if all items start with the defined prefix
    while len(common_prefix) >= 1:
        if all([item.startswith(common_prefix) for item in strs]):
            break
        # if items do not start with same prefix, shorten prefix by -1 position
        common_prefix = common_prefix[:-1]
    print (common_prefix)


if __name__ == "__main__":
    strs = ["flight", "flow", "fur"]
    longest_common_prefix(strs)
