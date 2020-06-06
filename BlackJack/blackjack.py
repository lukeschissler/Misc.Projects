from random import shuffle
from AIs import random_ai


class Card:
    def __init__(self, val: str, suit: str) -> None:
        self.val = val
        self.suit = suit

    def __repr__(self) -> str:
        return f"{self.val} of {self.suit}"


class Deck:
    def __init__(self, num=1) -> None:
        self.num = num
        self.deck_reset()

    def deck_reset(self) -> None:
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        vals = [str(x) for x in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
        self.deck = [Card(x, y) for x in vals for y in suits] * self.num

    def shuffle(self) -> None:
        shuffle(self.deck)

    def deal(self, size) -> list:
        """Implement more true to life deal"""
        return [self.deck.pop() for x in range(size)]


class BlackJack:
    def __init__(self, players, deck_num=1, turns=1, dealer = ['Dealer']) -> None:
        self.players = players + dealer
        self.deck_num = deck_num
        self.ais = [random_ai]
        self.score_card = {player : []  for player in self.players}
        self.turns = turns
        self.deck = Deck(deck_num)

    def deal(self) -> None:
        if len(self.deck.deck) < len(self.players) * 2:
            self.deck.deck_reset()
            self.deck.shuffle()
        else:
            self.game_state = {x: self.deck.deal(2) for x in self.players}

    def sum_hand(self, hand) -> set:
        sums = [0]
        for card in hand:
            if card.val in ["Jack", "Queen", "King"]:
                sums = [x + 10 for x in sums]
            elif card.val == "Ace":
                sums = [x + 1 for x in sums] + [x + 11 for x in sums]
            else:
                sums = [x + int(card.val) for x in sums]
        return sorted(set(sums))

    def turn(self, player) -> None:
        hand = self.game_state[player]
        print(f"Your hand is: {hand}. Possible sums: {self.sum_hand(hand)}")

        while True:

            hit = int(input("Hit? (0/1) "))

            if hit:
                self.game_state[player].append(self.deck.deck.pop())
                hand = self.game_state[player]
                hand_sum = self.sum_hand(hand)
            else:
                break

            if 21 in hand_sum:
                print(f"Your hand is: {hand}. Your sum is 21.")
                break
            elif all(i > 21 for i in hand_sum):
                print(f"Your hand is {hand}. You busted at {hand_sum}")
                break
            else:
                print(f"Your hand is: {hand}. Possible sums: {hand_sum}")

    def ai_play(self, ai) -> None:
        while True:

            hit = ai()

            if hit:
                self.game_state[ai].append(self.deck.deck.pop())
                hand = self.game_state[ai]
                hand_sum = self.sum_hand(hand)
            else:
                break

            if 21 in hand_sum:
                break
            elif all(i > 21 for i in hand_sum):
                break
            else:
                pass

        print(f"{ai.__name__}'s final hand is {self.game_state[ai]}")

    def play(self) -> None:
        self.deck.shuffle()
        for i in range(self.turns):
            self.deal()

            for player in self.players:
                if player in self.ais:
                    self.ai_play(player)
                else:
                    self.turn(player)

            self.assess()


    def assess(self) -> str:
        for player in self.players:
            hand_sums = [x for x in self.sum_hand(self.game_state[player]) if x < 22]
            if not hand_sums:
                self.score_card[player].append(0)
            else:
                self.score_card[player].append(max(hand_sums))

        print('\n'.join([f"{x} ended with a score of {y[-1]}." if y[-1] else f"{x} busted!" for x,y in self.score_card.items()]))

def main():
    game = BlackJack([random_ai], deck_num=4, turns=100, dealer = [])
    game.play()
    print(game.score_card[random_ai])



if __name__ == "__main__":
    main()
