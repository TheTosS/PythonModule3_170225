import random
# Возьмите классы Deck и Card с GIST'а занятия. Доработайте классы, если требуется.
class Card:
    DIAMONDS = "Diamonds"
    HEARTHS = "Hearts"
    SPADES = "Spades"
    CLUBS = "Clubs"
    def __init__(self, value, suit):
        self.__value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.__suit = suit  # Масть карты

    def __repr__(self):
        icons = {
            "Diamonds": '\u2666',
            "Hearts": "\u2665",
            "Spades": '\u2660',
            "Clubs": '\u2663'
        }
        return f"{self.__value}{icons[self.__suit]}"

    def equal_suit(self, other_card):
        return self.__suit == other_card.suit

    @property
    def value(self):
        return self.__value

    def __gt__(self, other_card):
        index_value_card1 = Deck.values.index(self.__value)
        index_value_card2 = Deck.values.index(other_card.value)
        if index_value_card1 > index_value_card2:
            return True
        elif index_value_card1 < index_value_card2:
            return False
        else:  # Значения карт равны
            index_suit_card1 = Deck.suits.index(self.__suit)
            index_suit_card2 = Deck.suits.index(other_card.suit)
            return index_suit_card1 > index_suit_card2

    def __lt__(self, other_card):
        return not self.__gt__(other_card)

    # Добавляем метод, возвращающий кол-во очков для каждой карты
    def points(self):
        return Deck.card_points[self.__value]


class Deck:
    # Количество очков, которые дают карты
    card_points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    suits = ("Clubs", "Spades", "Diamonds", "Hearts")

    def __init__(self):  # magic-method
        self.cards = []
        self.last_index_card = 0
        for suit in Deck.suits:
            for value in Deck.values:
                card = Card(value, suit)
                self.cards.append(card)

    def __str__(self):
        cards_str = []
        for card in self.cards:
            cards_str.append(card.__str__())
        return f"deck[{len(self.cards)}]:" + ", ".join(cards_str)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            card = self.cards[self.last_index_card]
        except IndexError:
            raise StopIteration
        self.last_index_card += 1
        return card

    def draw(self, x) -> list:
        hand = self.cards[:x]
        self.cards = self.cards[x:]
        return hand

    def shuffle(self) -> None:
        random.shuffle(self.cards)
