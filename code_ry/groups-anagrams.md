# groups anagrams



```python
from collections import defaultdict

def group_anagrams(strs):
    # Create a defaultdict to store anagrams, where the key is the sorted string and the value is a list of original strings.
    anagrams = defaultdict(list)

    # Iterate through each string in the input list.
    for s in strs:
        # Create a copy of the original string before sorting.
        original = s

        # Sort the characters of the string in lexicographical order.
        sorted_s = ''.join(sorted(s))

        # Use the sorted string as a key in the defaultdict and append the original string to the corresponding list.
        anagrams[sorted_s].append(original)

    # Convert the values of the defaultdict to a list to get the final result of grouped anagrams.
    result = list(anagrams.values())

    return result

# Example usage:
input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_anagrams(input_strs)

# Print the grouped anagrams.
for group in output:
    print(group)

```
