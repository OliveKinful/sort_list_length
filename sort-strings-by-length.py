def sort_strings_by_length(strings):
    return sorted(strings, key=len)

#creating strings in a list
strings = ["apple", "banana", "orange", "strawberry", "cranberry"]
sorted_strings = sort_strings_by_length(strings)
print("Sorted strings by length:", sorted_strings)