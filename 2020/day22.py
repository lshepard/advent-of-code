player1 = """48
23
9
34
37
36
40
26
49
7
12
20
6
45
14
42
18
31
39
47
44
15
43
10
35"""

player2 = """13
19
21
32
27
16
11
29
41
46
33
1
30
22
38
5
17
4
50
2
3
28
8
25
24"""

player1 = list(reversed([int(c.strip()) for c in player1.split("\n")]))
player2 = list(reversed([int(c.strip()) for c in player2.split("\n")]))


p1i = 0
p2i = 0

"""
Recursive Combat still starts by splitting the cards into two decks (you offer to play with the same starting decks as before - it's only fair). Then, the game consists of a series of rounds with a few changes:

Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1. Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top card of their deck as normal.

If both players have at least as many cards remaining in their deck as the value of the card they just drew, the winner of the round is determined by playing a new game of Recursive Combat (see below).
Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round is the player with the higher-value card.
"""

#scores  = set()
# stores configuration and the score at that time

def key(player1, player2):
    return "p1: " + ",".join([str(c) for c in player1]) + " p2:" + ",".join([str(c) for c in player2])

game_count=0
def recursive_game(player1, player2, depth=1):
    """Returns winner, player1 deck, player2 deck"""
    global game_count
    round = 0
    game_count += 1
    game = game_count
    print(f"--- Entering subgame {game} at depth {depth} --")
    print("")
    print(f"Player 1 has {len(player1)} cards")
    print(f"Player 2 has {len(player2)} cards")
    
    scores = set()
    while len(player1) > 0 and len(player2) > 0:
        round += 1
        # check for previous round
        k = key(player1, player2)
        if k in scores:
            
            return (1, player1, player2)
        scores.add(k)

        print("")
        print(f"-- Round {round} (Game {game}) --")
        print(f"Player 1's deck: {', '.join([str(c) for c in reversed(player1)])}")
        print(f"Player 2's deck: {', '.join([str(c) for c in reversed(player2)])}")

        p1card = player1.pop()
        p2card = player2.pop()
        
        print(f"Player 1 plays: {p1card}")
        print(f"Player 2 plays: {p2card}")
        
        if p1card <= len(player1) and p2card <= len(player2):
            print("Playing a subgame ...")
            g = recursive_game(player1[-p1card:], player2[-p2card:], depth+1)
            winner = g[0]
            
            print(f"... back to game {game} at depth {depth}")
        else:
            if p1card > p2card:
                winner = 1
            else:
                winner = 2
                
        if winner == 1:
            player1 = [p2card, p1card] + player1
        else:
            player2 = [p1card, p2card] + player2
        print(f"Player {winner} wins round {round} of game {game}!")
    
    return (winner, player1, player2)

winner, p1, p2 = recursive_game(player1, player2)

if winner == 1:
    winning_cards = p1
else:
    winning_cards = p2

print(winning_cards)
print(sum([card*(i+1) for i, card in enumerate(winning_cards)]))
    
    
    
