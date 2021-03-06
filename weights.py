# 2. Weights using tuples
weights = [70, 80, 45, 50]
print('Initial list:')
print(weights)

maximum = max(weights)
minimum = min(weights)
print('Maximum:', maximum)
print('Minimum:', minimum)

weights[weights.index(45)] = 48
print('After updating list:')
print(weights)

total = sum(weights)
print('Sum of weights: ', total)
mean = total / len(weights)
print('Mean:', mean)
