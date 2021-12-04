import re
import fileinput


lines = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".split("\n")

lines = list(fileinput.input())


def main(lines):
    random_ordering = [int(c) for c in lines[0].split(",")]

    boards = []
    num_boards = int((len(lines) - 1) / 6)
    for i in range(num_boards):
        board_lines = lines[i * 6 + 2:i * 6 + 7]
        print(board_lines)
        boards.append(BingoBoard(board_lines))

    print(boards)

    for i,num in enumerate(random_ordering):
        for board in boards:
            res = board.play(random_ordering[:i+1])
            if res:
                print("Winner!")
                print(board)
                score = board.score()
                print(f"score {score} num {num}")
                return score * num

class BingoBoard():
    def __init__(self, bingo_lines):
        board = []
        for line in bingo_lines:
            if len(line) > 0:
                print(line)
                board.append([int(i) for i in re.split(" +", line.strip())])

        self.board = list(reversed(board))

    def __repr__(self): 
        s = ""
        for row in self.board:
            for c in row:
                s += str(c)
                s += "\t"
            s += "\n"
        return s
    
    def play(self, nums):
        """Statelessly play a series of numbers"""
#        print(f"Playing {nums}")

        self.played_nums = nums
        
        for row in self.board:
            # did the row hit?
            if len([c for c in row if c not in nums]) == 0:
                return True

        # by cols
        for i in range(len(self.board[0])):

            # did the col hit?
            col = [row[i] for row in self.board]
            if len([c for c in col if c not in nums]) == 0:
                return True
        
        return False

    def score(self):
        s = 0
        for row in self.board:
            for c in row:
                if c not in self.played_nums:
                    print("score calc " + str(c))
                    s += c
        return s
        
b = BingoBoard("""22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19""".split("\n"))

assert(b.play([22,13,17,11,0]))
assert(b.play([22,8,21,6,1]))

print(main(lines))
