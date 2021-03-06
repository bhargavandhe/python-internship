input_ = [(4, 5), (2, 3), (6, 7), (2, 8)]
print("The original list of tuple is: ", input_)
lst = len(input_)
for i in range(lst):
    for j in range(lst - i - 1):
        if (input_[j][0] + input_[j][1]) > (input_[j + 1][0] + input_[j + 1][1]):
            input_[j], input_[j + 1] = input_[j + 1], input_[j]
print("\nAfter sorting tuples, the answer is: ", input_)
