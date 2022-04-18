import random
card=["spades","Clubs","Diamond","Heart"]
ranks=[1,2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
def rand_card():
    rand_card=random.choice(card)
    random_ranks=random.choice(ranks)
    print(f"The[{rand_card}] of [{random_ranks}]")
rand_card()