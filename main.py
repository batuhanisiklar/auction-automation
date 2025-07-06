from auctionLogo import logo
print(logo)
name_box = []
bid_box = []
cnt = 0
most_bid = 0
while cnt == 0:
  name = input("What is your name?:")
  bid = int(input("What is your bid? :"))
  if bid > most_bid:
    most_bid = bid
    name_box = [name]
    bid_box = [bid]
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if other_bidders == "no" or other_bidders == "No" or other_bidders == "NO":
    cnt = 1
  elif other_bidders == "Yes" or other_bidders == "yes" or other_bidders == "YES":
    cnt = 0
  else:
    cnt = 1
print("The winner is", name_box[0], "with a bid of $", bid_box[0], ".")
