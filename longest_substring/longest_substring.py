# identify the longest substring in a given string, which only contains unique letters

text_snippet = "abcabcbb"

n = len(text_snippet)
my_dict = {}
i = 0
res = 0

for upper_bound in range(n):
    if text_snippet[upper_bound] in my_dict:
        i = max(my_dict[text_snippet[upper_bound]],i)

    res = max(res, upper_bound-i + 1)
    my_dict[text_snippet[upper_bound]] = upper_bound +1

print(res)
