import random


def main():
    name = (input("Enter your name: "))
    print(f"Hello, {name}")

    score = check_scores(name)

    variety = input().split(",")
    if not variety[0]:
        variety = ["rock", "paper", "scissors"]

    print("Okay, let's start")

    scores = round_process(variety, score)


def check_scores(name):
    with open("rating.txt") as rating:
        for line in rating:
            if name in line:
                score = int(line.split()[-1])
                break
        else:
            score = 0
    return score


def round_process(variety, score):
    while True:
        user = input()
        if user == "!exit":
            print("Bye!")
            break
        elif user == "!rating":
            print("Your rating:", score)
            continue
        elif user not in variety:
            print("Invalid input")
            continue
        user = variety.index(user)

        comp = random.choice(range(len(variety)))

        score += check_turn(user, comp, variety)

    return score


def check_turn(user, comp, variety):
    if user == comp:
        print(f"There is a draw ({variety[user]})")
        return 50
    else:
        lose = []
        for n in range(1, (len(variety) - 1) // 2 + 1):
            lose.extend([n + user if n + user < len(variety)
                         else n + user - len(variety)])

        if comp in lose:
            print(f"Sorry, but the computer chose {variety[comp]}")
            return 0
        else:
            print(f"Well done. The computer chose {variety[comp]} and failed")
            return 100


main()
