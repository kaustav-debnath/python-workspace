from art import logo
print(f"{logo}\nWelcome to the secret auction program\n")

# TODO-4: Compare bids in dictionary
def find_highest_bidder(auction_data):
    highest_bidder=0
    highest_bidder_key = ""
    for key in auction_data:
        if auction_data[key] > highest_bidder:
            highest_bidder = auction_data[key]
            highest_bidder_key = key
    print(f"{highest_bidder_key} is the highest bidder with the bid value ${auction_data[highest_bidder_key]}")

should_continue = True
auction_data = {}
while should_continue:
    # TODO-1: Ask the user for input
    name = input("What is your name?:\t")
    bid = input("What's your bid?:\t$")
    # TODO-2: Save data into dictionary {name: price}
    auction_data[name] = int(bid)
    # TODO-3: Whether if new bids need to be added
    more_bidders = input("Are there other bidders type yes or no?: ")
    print("\n"*100)
    if more_bidders.lower() == "no":
        should_continue = False
find_highest_bidder(auction_data)

