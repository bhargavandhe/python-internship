# 1. Fruit colors using dictionaries
fruits = {
    'apple': 'green',
    'banana': 'yellow',
    'cherry': 'red'
}

print('Initial dictionary')
print(fruits)

print('Changing color of apple to red')
fruits['apple'] = 'red'
print(fruits)

print('Adding entry for guava')
fruits['guava'] = 'green'
print(fruits)

print('Removing cherry from dictionary')
del fruits['cherry']
print(fruits)
