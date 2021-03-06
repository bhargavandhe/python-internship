# 2. To save odd, even and prime numbers into separate lists
numbers: list = [17, 81, 44, 99, 53, 26, 70, 89]
odd, even, prime = ([] for _ in range(3))
for number in numbers:
    even.append(number) if number % 2 == 0 else odd.append(number)

    isPrime: bool = False
    for i in range(2, number):
        if number % i == 0:
            isPrime = True
            break
    if not isPrime:
        prime.append(number)

print('Odd numbers:', odd)
print('Even numbers:', even)
print('Prime numbers:', prime)
print('Maximum element: ', max(numbers))
print('Minimum element: ', min(numbers))
