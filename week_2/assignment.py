import re

handle = open("regex_sum_48980.txt")
data_text = handle.read()

list_numbers = re.findall("[0-9]+", data_text)
list_integers = list(map(int, list_numbers))

result = sum(list_integers) 
print(result)