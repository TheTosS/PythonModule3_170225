from classes import Card

def sum_points(cards):
    """
    Напишите отдельную функцию для нахождения суммы очков всех карт в списке
    :param cards: список карт(рука игрока или диллера)
    :return: сумму очков
    """
    # Совет: храните кол-во очков за карту внутри класса Колоды(колода "знает", сколько дает очков каждая карта)

    #  Сначала считаем сумму карт, считая ТУЗ за 11-очков
    sum_points = 0
    for card in cards:
        sum_points += card.points()
    # Если сумма > 21, то перечитываем сумму, считая ТУЗ за 1(единицу)
    if sum_points > 21:
        for card in cards:
            if card.value == "A":
                sum_points -= 10

    return sum_points


print(sum_points([Card("10", Card.SPADES), Card("A", Card.DIAMONDS)]))
print(sum_points([Card("8", Card.SPADES), Card("Q", Card.DIAMONDS), Card("A", Card.DIAMONDS)]))
print(sum_points([Card("A", Card.DIAMONDS), Card("A", Card.DIAMONDS)]))