import random
friends = ["Alice", "Bob", "Charlie", "David", "Emmanuel"]
# Option 1
choose_random_friend = random.randint(0, len(friends) -1)
print(f"Random chosen card is for {friends[choose_random_friend]}")
# Option 2
print(f"Random chosen card is for {random.choice(friends)}")