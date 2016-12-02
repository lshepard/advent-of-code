# --- Day 2: Bathroom Security ---
#
# You arrive at Easter Bunny Headquarters under cover of darkness. However, you left in such a
# rush that you forgot to use the bathroom! Fancy office buildings like this one usually have
# keypad locks on their bathrooms, so you search the front desk for the code.
#
# "In order to improve security," the document you find says, "bathroom codes will no longer
# be written down. Instead, please memorize and follow the procedure below to access the bathrooms."
#
# The document goes on to explain that each button to be pressed can be found by starting on the
# previous button and moving to adjacent buttons on the keypad: U moves up, D moves down, L moves 
# left, and R moves right. Each line of instructions corresponds to one button, starting at the 
# previous button (or, for the first line, the "5" button); press whatever button you're on at the 
# end of each line. If a move doesn't lead to a button, ignore it.
#
# You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom. You picture a keypad like this:
#
# 1 2 3
# 4 5 6
# 7 8 9
#
# Suppose your instructions are:
# 
# ULL
# RRDDD
# LURDL
# UUUUD
# You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.
# Starting from the previous button ("1"), you move right twice (to "3") and then down three times (stopping at "9" after
# two moves and ignoring the third), ending up with 9.
# Continuing from "9", you move left, up, right, down, and left, ending with 8.
# Finally, you move up four times (stopping at "2"), then down once, ending with 5.
# So, in this example, the bathroom code is 1985.
# 
# Your puzzle input is the instructions from the document you found at the front desk. What is the bathroom code?

#--- Part Two ---

# You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many
# fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's 
# dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds 
# of man-hours of bathroom-keypad-design meetings:
#
#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D
#
# You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome 
# is very different:
#
# You start at "5" and don't move at all (up and left are both edges), ending at 5.
# Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
# Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
# Finally, after five more moves, you end at 3.
# So, given the actual keypad layout, the code would be 5DB3.
#
# Using the same instructions in your puzzle input, what is the correct bathroom code?
#

class Day2
  def self.bathroom_code(rows, apply_move_fn)
    remaining_codes(5, rows.split("\n"), apply_move_fn).join("")
  end

  # given a starting number and a set of rows, this will return all the remaining numbers that would be called
  def self.remaining_codes(starting_number, remaining_rows, apply_move_fn)
    if remaining_rows.empty?
      []
    else
      this_row = remaining_rows.shift
      this_digit = digit_for_row(starting_number, this_row.chars, apply_move_fn)
      
      [this_digit] + remaining_codes(this_digit, remaining_rows, apply_move_fn)
    end
  end

  # given a starting number and a set of instructions (array of directions), return 
  # the final number
  # this works recursively -- that is, if you start with [5, "UL"], then that could apply the first and then return [2, "L"], etc
  def self.digit_for_row(starting_number, instructions, apply_move_fn)
    number = starting_number
    instructions.each do |instruction|
      number = self.send(apply_move_fn, number, instruction)
    end
    number
  end

  # takes a number and moves in a single direction for a naive keypad
  # 1 2 3
  # 4 5 6
  # 7 8 9
  def self.simple_keypad_apply_move(starting_number, instruction)
    {
      1 => { 'U' => 1, 'L' => 1, 'R' => 2, 'D' => 4 },
      2 => { 'U' => 2, 'L' => 1, 'R' => 3, 'D' => 5 },
      3 => { 'U' => 3, 'L' => 2, 'R' => 3, 'D' => 6 },
      4 => { 'U' => 1, 'L' => 4, 'R' => 5, 'D' => 7 },
      5 => { 'U' => 2, 'L' => 4, 'R' => 6, 'D' => 8 },
      6 => { 'U' => 3, 'L' => 5, 'R' => 6, 'D' => 9 },
      7 => { 'U' => 4, 'L' => 7, 'R' => 8, 'D' => 7 },
      8 => { 'U' => 5, 'L' => 7, 'R' => 9, 'D' => 8 },
      9 => { 'U' => 6, 'L' => 8, 'R' => 9, 'D' => 9 },
    }[starting_number][instruction]
  end

  #     1
  #   2 3 4
  # 5 6 7 8 9
  #   A B C
  #     D
  def self.complex_keypad_apply_move(starting_number, instruction)
    {
      1 => { 'U' => 1, 'L' => 1, 'R' => 1, 'D' => 3 },
      2 => { 'U' => 2, 'L' => 2, 'R' => 3, 'D' => 6 },
      3 => { 'U' => 1, 'L' => 2, 'R' => 4, 'D' => 7 },
      4 => { 'U' => 4, 'L' => 3, 'R' => 4, 'D' => 8 },
      5 => { 'U' => 5, 'L' => 5, 'R' => 6, 'D' => 5 },
      6 => { 'U' => 2, 'L' => 5, 'R' => 7, 'D' => 'A' },
      7 => { 'U' => 3, 'L' => 6, 'R' => 8, 'D' => 'B' },
      8 => { 'U' => 4, 'L' => 7, 'R' => 9, 'D' => 'C' },
      9 => { 'U' => 9, 'L' => 8, 'R' => 9, 'D' => 9 },
      'A' => { 'U' => 6, 'L' => 'A', 'R' => 'B', 'D' => 'A' },
      'B' => { 'U' => 7, 'L' => 'A', 'R' => 'C', 'D' => 'D' },
      'C' => { 'U' => 8, 'L' => 'B', 'R' => 'C', 'D' => 'C' },
      'D' => { 'U' => 'B', 'L' => 'D', 'R' => 'D', 'D' => 'D' }
    }[starting_number][instruction]
  end

  def self.main
    input = File.read("inputs/day2.txt")
    puts "Part 1 : #{Day2.bathroom_code(input, :simple_keypad_apply_move)}"
  end

end

Day2.main
