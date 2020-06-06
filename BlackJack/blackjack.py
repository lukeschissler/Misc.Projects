from random import shuffle
from AIs import random_ai

class Card:

    def __init__(self, val:str, suit:str) -> None:
        self.val = val
        self.suit = suit

    def __repr__(self) -> str:
        return f'{self.val} of {self.suit}'

class Deck:

    def __init__(self) -> None:
        self.deck_reset()

    def deck_reset(self) -> None:
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        vals = [str(x) for x in range(2, 11)] + ['Jack', 'Queen', 'King', 'Ace']
        self.deck = [Card(x, y) for x in vals for y in suits]

    def shuffle(self) -> None:
        shuffle(self.deck)

    def deal(self, size) -> list:
        """Implement more true to life deal"""
        return [self.deck.pop() for x in range(size)]

class BlackJack:

    def __init__(self, players, decks=1) -> None:
        self.players =  players + ['Dealer']
        self.deck = Deck()
        self.ais = ['random_ai']

    def deal(self) -> None:
        self.deck.shuffle()
        self.game_state = {x : self.deck.deal(2) for x in self.players }

    def sum_hand(self, hand) -> set:
        sums = [0]
        for card in hand:
            if card.val in ['Jack', 'Queen', 'King']:
                sums = [x + 10 for x in sums]
            elif card.val == 'Ace':
                sums = [x + 1 for x in sums ] + [x+11 for x in sums]
            else:
                sums = [x + int(card.val) for x in sums]
        return set(sums)

    def turn(self, player) -> None:
        hand = self.game_state[player]
        print(f'Your hand is: {hand}. Possible sums: {self.sum_hand(hand)}')

        while True:

            hit = int(input('Hit? (0/1) '))

            if hit:
                self.game_state[player].append(self.deck.deck.pop())
                hand = self.game_state[player]
                hand_sum = self.sum_hand(hand)
            else:
                break

            if 21 in hand_sum:
                print(f'Your hand is: {hand}. Your sum is 21.')
                break
            elif all(i > 21 for i in hand_sum):
                print(f'Your hand is {hand}. You busted at {hand_sum}')
                break
            else:
                print(f'Your hand is: {hand}. Possible sums: {hand_sum}')

    def ai_play(self, ai) -> None:
        pass

    def play(self) -> None:
        self.deal()

        for player in self.players:
            if player in self.ais:
                self.ai_play(player)
            else:
                self.turn(player)

        self.assess()

    def assess(self) -> str:
        final_scores = []
        for player in self.players:
            hand_sum = self.sum_hand(self.game_state[player])
            if all(i > 21 for i in hand_sum):
                final_scores.append((0, player))
            else:
                hand_sum = {x for x in hand_sum if x < 22}
                final_scores.append((max(hand_sum), player))
        print('\n'.join([f'{y} ended with a score of {x}.' if x else f'{y} busted!' for x, y in sorted(final_scores,
                                                                                        reverse= True, key = lambda x: x[0])]))


def main():
    game = BlackJack(['Tim', 'Jack'])
    game.play()

if __name__ == '__main__':
    main()