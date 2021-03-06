# 1. List of characters containing A-Z using list comprehension
char_list = [chr(char) for char in range(ord('A'), ord('Z') + 1)]
print(char_list)

# 2. Dictionary of characters containing character as key and its Unicode as value using list comprehension
char_dict = {char: ord(char) for char in char_list}
print(char_dict)

# 3. Dictionary of characters containing only vowel characters as key and their Unicode as value
vowel_char_dict = {char: char_dict[char] for char in char_dict if char in ['A', 'E', 'I', 'O', 'U']}
print(vowel_char_dict)

# 4. Generator object containing consonant as first value and its Unicode as second value using the above list
consonant_gen = ((char, ord(char)) for char in vowel_char_dict if char not in ['A', 'E', 'I', 'O', 'U'])
print(consonant_gen, type(consonant_gen))
