# To find frequency of each element of list and store them in various forms
numbers: list = [1, 2, 2, 4, 3, 7, 1, 9, 5, 4, 3, 3, 0, 7, 2]
freq: dict = {}

list_of_dictionary, list_of_lists, list_of_tuples = [], [], []

for number in numbers:
    if number not in freq:
        freq[number] = 1
    else:
        freq[number] += 1

for n in freq:
    list_of_dictionary.append({n: freq[n]})
    list_of_lists.append([n, freq[n]])
    list_of_tuples.append((n, freq[n]))

print(list_of_dictionary, list_of_lists, list_of_tuples, sep='\n')
