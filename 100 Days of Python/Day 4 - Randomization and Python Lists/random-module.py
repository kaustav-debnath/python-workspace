import random

# random_float = random.random()
# print(f"Random float between 0 and 1: {random_float}")
# random_integer = random.randint(1, 10)
# print(f"Random integer between 1 and 10: {random_integer}")

random_0_1 = random.randint(0, 1)
print_heads_or_tails = "Heads" if random_0_1 == 0 else "Tails"
print(f"The coin flip result is: {print_heads_or_tails}")