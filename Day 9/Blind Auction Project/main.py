# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
bids = {}
should_continue = True
while should_continue:
    name = input("Enter your name: ")
    bid = float(input("Enter your bid: $"))
    answer = input("There are other users that should make a bid? ").lower()
    bids[name] = bid
    if answer == "no":
        should_continue = False
    print("\n" * 20)

max_bid = float("-inf")
name = ""
for key, value in bids.items():
    if value > max_bid:
        max_bid = value
        name = key
print(f"The highest bid was {name}'s bid of: ${max_bid}")
