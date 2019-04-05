require 'set'

class Day8

  def self.pixels_turned_on(input)
    board = Board.new(50,6)
    input.split("\n").each do |row|
      board.execute_instruction(row)
    end
    board.cells.count
  end

  def self.display_board(input)
    board = Board.new(50,6)
    input.split("\n").each do |row|
      board.execute_instruction(row)
    end
    board.to_s
  end

  def self.main
    input = File.read("inputs/day8.txt")
    puts "Part 1: #{Day8.pixels_turned_on(input)}"
    puts "Part 2: \n#{Day8.display_board(input)}"
  end

end

class Board
  def initialize(width, height)
    @width = width
    @height = height
    @cells = Set.new
  end

  def cells
    @cells
  end

  # parses out the instructions and fields and passes them along
  # rect AxB                =>    rect(A,B)
  # rotate row y=A by B     =>  rotate_row(A,B)
  # rotate column x=A by B  =>  rotate_column(A,B)
  def execute_instruction(instruction)
    if m = /rect (\d+)x(\d+)/.match(instruction)
      rect(m[1].to_i, m[2].to_i)
    elsif m = /rotate row y=(\d+) by (\d+)/.match(instruction)
      rotate_row(m[1].to_i, m[2].to_i)
    elsif m = /rotate column x=(\d+) by (\d+)/.match(instruction)
      rotate_column(m[1].to_i, m[2].to_i)
    else
      raise
    end
  end

  # rect AxB turns on all of the pixels in a rectangle at the 
  # top-left of the screen which is A wide and B tall.
  def rect(a,b)
    new_cells = a.times.flat_map do |x|
      b.times.flat_map do |y|
        Cell.new(x,y,@width,@height)
      end
    end

    @cells.merge(new_cells)
  end

  # rotate row y=A by B shifts all of the pixels in row A 
  # (0 is the top row) right by B pixels. Pixels that would fall 
  # off the right end appear at the left end of the row.
  def rotate_row(y,num)
    row_cells = @cells.select {|c| c.y == y}
    new_cells = row_cells.map {|c| c.rotate(num,0)}
    @cells.subtract(row_cells)
    @cells.merge(new_cells)
  end

  # rotate column x=A by B shifts all of the pixels in column A 
  # (0 is the left column) down by B pixels. Pixels that would fall
  # off the bottom appear at the top of the column.
  def rotate_column(x,num)
    col_cells = @cells.select {|c| c.x == x}
    new_cells = col_cells.map {|c| c.rotate(0,num)}
    @cells.subtract(col_cells)
    @cells.merge(new_cells)
  end

  def to_s
    display = Array.new(@height) { Array.new(@width, " ") }
    @cells.each do |cell|
      display[cell.y][cell.x] = "#"
    end
    display.map {|row| row.join("")}.join("\n")
  end
  
end

class Cell
  attr_accessor :x, :y
  def initialize(x,y,w,h)
    @x = x
    @y = y
    @w = w
    @h = h
  end

  # move a given number of spaces right, then the same number down,
  # rotating to the top of the board if need be
  # this will return a new cell
  def rotate(right,down)
    Cell.new((@x + right) % @w,
             (@y + down) % @h,
             @w,
             @h)
  end

  def coords
    [@x, @y]
  end

  def hash
    {x: @x, y: @y, w: @width, h: @height}.hash
  end
end

if __FILE__==$0
  Day8.main
end
