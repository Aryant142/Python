import itertools , random
deck = list(itertools.product(range(1,14),['spade','heart','club','diamond']))
random.shuffle(deck)
for i in range (5):
    print(deck[i])
