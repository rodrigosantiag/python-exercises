import itertools

def poker_hand_rank(hand):
    # Sort the cards in the hand
    sorted_hand = sorted(hand, key=lambda card: (card[0], card[1]))
    ranks = [card[0] for card in sorted_hand]
    freqs = [ranks.count(rank) for rank in set(ranks)]

    # Check for high card, pair, two pairs, three of a kind, straight, flush,
    # full house, four of a kind, and straight flush
    if freqs == [1, 1, 1, 1, 1]:
        return (8, sorted_hand)
    elif freqs == [2, 2, 1]:
        return (7, sorted_hand)
    elif freqs == [2, 1, 1, 1]:
        return (6, sorted_hand)
    elif freqs == [3, 1, 1]:
        return (5, sorted_hand)
    elif freqs == [4, 1]:
        return (1, sorted_hand)
    elif freqs == [3, 2]:
        return (5, sorted_hand)
    elif sorted_hand[-1][0] == '5' and all(x[0] == sorted_hand[0][0] for x in sorted_hand):
        return (4, sorted_hand)
    elif all(x[1] == sorted_hand[0][1] for x in sorted_hand):
        flush_ranks = [x[0] for x in sorted_hand]
        if sorted(flush_ranks) == list('23456789TJQKA'):
            return (3, sorted_hand)
        elif sorted(flush_ranks) == list('A2345'):
            return (4, sorted_hand)
        else:
            return (2, sorted_hand)
    elif sorted_hand[-1][0] == '5' and all(x[0] == sorted_hand[0][0] for x in sorted_hand) and all(x[1] == sorted_hand[0][1] for x in sorted_hand):
        return (0, sorted_hand)
    else:
        return (-1, sorted_hand)


def best_hands(hands):
    hand_ranks = [poker_hand_rank(hand) for hand in hands]
    max_rank = max(hand_ranks, key=lambda x: x[0])
    return [hand for rank, hand in hand_ranks if rank == max_rank]
