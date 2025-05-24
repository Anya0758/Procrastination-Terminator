import random
from typing import Literal


class Card:
    def __init__(self, id: int, name: str, duration: int, ctype: Literal['entertainment', 'study', 'exercise'],
                 base_prob: float):
        self.id = id
        self.name = name
        self.duration = duration
        self.ctype = ctype
        self.base_prob = base_prob
        self.current_prob = base_prob

    def showCardInfo(self):
        print(f"{self.name} for {self.duration} minutes, which is a {self.ctype} event.")

    def showCardProbability(self):
        print(f"{self.name}'s drawn probability: {self.current_prob}")


INITIAL_CARDS = [
    Card(1, 'Play games', 30, 'entertainment', 0.05),
    Card(2, 'Watch TV', 20, 'entertainment', 0.05),
    Card(3, 'Do homework', 40, 'study', 0.25),
    Card(4, 'Memorize words', 15, 'study', 0.10),
    Card(5, 'Reading extracurricular book', 30, 'study', 0.20),
    Card(6, 'Stretch', 10, 'exercise', 0.15),
    Card(7, 'Take a deep breath', 5, 'exercise', 0.10),
    Card(8, 'rope skipping', 15, 'exercise', 0.10)
]


def draw_card(cards):
    r = random.uniform(0, 1)
    prob = 0
    for card in cards:
        if prob + card.current_prob >= r:
            return card
        prob += card.current_prob


def main():
    score = 0
    cards = INITIAL_CARDS
    print("Welcome to the anti-procrastination gacha mini-game!")
    print("You can enter 'draw' to draw a card, 'status' to check the status, and 'exit' to exit the game")

    while True:
        cmd = input("Please enter the command: (draw/status/exit/score):").strip().lower()
        if cmd == 'draw':
            card = draw_card(cards)
            card.showCardInfo()
            if card.ctype == 'entertainment':
                cards = INITIAL_CARDS
            else:
                card.current_prob = round((card.current_prob - 0.05), 3)
                cards[0].current_prob = round((cards[0].current_prob + 0.025), 3)
                cards[1].current_prob = round((cards[1].current_prob + 0.025), 3)
            score += 1
            if score >= 10:
                print("You have finished today's challenge. Congratulations!")
                break
        elif cmd == 'status':
            print("Card draw probability: ")
            for card in cards:
                card.showCardProbability()
        elif cmd == 'exit':
            print("Thank you for your participation. Goodbye!")
            break
        elif cmd == 'score':
            print(f"You score is {score}.")
        else:
            print("Invalid command. Please enter (draw/status/exit/score).")


if __name__ == "__main__":
    main()