import random

score = 0
num = 0
while True:
    ask = input("What is 1+1:")
    if ask == "2":
        score += 1
    things = [
        "Planet:Common", "UFO:Rare", "Spaceship:Epic", "Astronaut:Legendary",
        "Black Hole:Chroma"
    ]
    chance = [90, 9, 1, 0.5, 0.03]
    op = input("OPEN:")
    if op == "y":
        numask = int(input("HOW MANY:"))
        if score < numask:
            print("Not Enough Score")
        else:
            results = random.choices(things, chance, k=numask)
            from collections import Counter
            print(Counter(results))
            score = score - numask
    else:
        pass
    print("Score:", score)
