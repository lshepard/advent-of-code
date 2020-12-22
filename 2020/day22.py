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

player1 = """9
2
6
3
1"""

player2 = """5
8
4
7
10"""

player1 = list(reversed([int(c.strip()) for c in player1.split("\n")]))
player2 = list(reversed([int(c.strip()) for c in player2.split("\n")]))


p1i = 0
p2i = 0

while len(player1) > 0 and len(player2) > 0:

    p1card = player1.pop()
    p2card = player2.pop()

    print( "---")
    print("player1" , p1card)
    print("player2", p2card)
    if p1card > p2card:
        player1 = [p2card, p1card] + player1
    else:
        player2 = [p1card, p2card] + player2

    print(player1, player2)

if len(player1) > 0:
    winning_cards = player1
else:
    winning_cards = player2

print(winning_cards)
print(sum([card*(i+1) for i, card in enumerate(winning_cards)]))
    
    
    
