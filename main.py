#!/usr/bin/env python

from itertools import cycle
import numpy as np

MAX_CARDS = 6
SKIP = 2


if __name__ == "__main__":
    n_players = int(input('[ NUMBER OF PLAYERS ] '))

    players = [input(f'\tplayer {i}: ') for i in range(n_players)]
    np.random.randint(n_players)
    max_cards = min(int(np.ceil(50 / n_players)), MAX_CARDS)
    rnds = list(range(max_cards, 0, -1*SKIP))
    rnds += reversed(rnds[:-1])

    print(f"[ PLAYERS ] {players}")
    print(f"[ rndS ] {rnds}")
    
    bids, trumps, wins, bids_won = {}, {}, {}, {player : 0 for player in players}
    for (rnd, n_cards), dealer in zip(enumerate(rnds), cycle(players)):
        bids[rnd] = {}
        n_bid = 0
        trumps[rnd] = input(f'[ ROUND {rnd} ] {dealer} deals {n_cards} cards. Enter trump suit to continue: ')
        if (rnd % n_players) == 0:
            bid_order = players[rnd+1:]
        else:
            bid_order = players[(rnd % n_players)+1:] + players[:(rnd % n_players)]
        print(f"[ BID ORDER ] {bid_order + [dealer]}")
        for player in bid_order:
            bids[rnd][player] = int(input(f"\t{player}'s bid ({n_bid} of {n_cards} has been bid): "))
            n_bid += bids[rnd][player]
        deal_str = f"{n_bid} of {n_cards} has been bid; "
        deal_str += "overbid: dealer can bid anything" if n_bid > n_cards else f"dealer cannot bid {n_cards - n_bid}"
        bids[rnd][dealer] = int(input(f"\t{dealer}'s bid ({deal_str}): "))
        print(f'[ BIDS ] {bids[rnd]}')
        wins[rnd] = [input(f"\ttrick {j} winner: ") for j in range(n_cards)]
        for player in players:
            n_tricks = len([x for x in wins[rnd] if x == player])
            print(f"\t{player} bid {bids[rnd][player]} with {n_tricks} tricks")
            bids_won[player] += (5 + n_tricks) if n_tricks == bids[rnd][player] else 0
        print(f"[ BIDS WON ] {bids_won}")







