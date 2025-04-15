"""
Write a generator that yields prime numbers indefinitely.
definition - a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11)
"""

prime_numbers = []

for i in range(2, 100):

    if i % 2 == 0 and i != 2:
        print(f"{i} is divisible by 2")
        continue
    elif i % 3 == 0 and i != 3:
        print(f"{i} is divisible by 3")
        continue
    elif i % 5 == 0 and i != 5:
        print(f"{i} is divisible by 5")
        continue
    elif i % 7 == 0 and i != 7:
        continue

    for j in prime_numbers:
        if i % j == 0:
            break
    else:
        prime_numbers.append(i)

print(prime_numbers)