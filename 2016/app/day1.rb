require 'csv'
require 'set'

# --- Day 1: No Time for a Taxicab ---
#
# Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's
# oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the 
# Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.
# 
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the 
# advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants 
# one star. Good luck!
#
# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is 
# as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves
# intercepted start here, and nobody had time to work them out further.
#
# The Document indicates that you should start at the given coordinates (where you just landed) 
# and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, 
# then walk forward the given number of blocks, ending at a new intersection.
#
# There's no time to follow such ridiculous instructions on foot, though, so you take a moment 
# and work out the destination. Given that you can only walk on the street grid of the city, 
# how far is the shortest path to the destination?
#
# For example:
#
# Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
# R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.
# How many blocks away is Easter Bunny HQ?

# --- Part Two ---
#
# Then, you notice the instructions continue on the back of the Recruiting Document. 
# Easter Bunny HQ is actually at the first location you visit twice.
#
# For example, if your instructions are R8, R4, R4, R8, the first location you visit 
# twice is 4 blocks away, due East.
#
# How many blocks away is the first location you visit twice?

class Day1

  def self.shortest_path_to_first_place_to_visit_twice(directions)
    
    path = coordinates([0,0],
                       [0,1],
                       directions.map {|s| s.gsub(/ +/, "")})

    visited = Set.new
    path.each do |coord|
      return coord[0].abs + coord[1].abs if visited.include?(coord)
      visited.add(coord)
    end
  end
  
  def self.shortest_path_from_origin(directions)

    path = coordinates([0,0],
                       [0,1],
                       directions.map {|s| s.gsub(/ +/, "")})

    coord = path.pop
    coord[0].abs + coord[1].abs 
  end
  
  # given the current direction and the letter of the turn ,
  # returns the new direction
  def self.next_direction(currently_facing, direction_to_turn)
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    offset = (direction_to_turn == "R" ? 1 : -1)
    directions[(directions.find_index(currently_facing) + offset) % 4]
  end

  # returns ALL coordinates - including in between ones
  def self.coordinates(origin, currently_facing, remaining_directions, visited_locations = nil)
    
    # base case
    if remaining_directions.empty?
      return []
    end

    # recursive algo
    current_direction = remaining_directions.shift
    direction_to_turn = current_direction.slice!(0)
    number_of_spaces = current_direction
    new_facing = next_direction(currently_facing, direction_to_turn)

    new_coordinates = number_of_spaces.to_i.times.map do |i|
      [ origin[0] + (new_facing[0] * (i+1)) , origin[1] + (new_facing[1] * (i+1)) ]
    end
    
#    puts "#{direction_to_turn}\t#{number_of_spaces}\t#{new_coordinates.inspect}"

    new_coordinates + coordinates(new_coordinates.last, new_facing, remaining_directions)
  end

  def self.main
    input = CSV.read("inputs/day1.txt").flatten
    puts "Part 1 : #{Day1.shortest_path_from_origin(input)}"
    puts "Part 2 : #{Day1.shortest_path_to_first_place_to_visit_twice(input)}"
  end
end

Day1.main

