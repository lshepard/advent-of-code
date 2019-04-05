# --- Day 3: Squares With Three Sides ---
#
# Now that you can think clearly, you move deeper into the labyrinth of hallways and office 
# furniture that makes up this part of Easter Bunny HQ. This must be a graphic design 
# department; the walls are covered in specifications for triangles.
#
# Or are they?
#
# The design document gives the side lengths of each triangle it describes, but... 
# 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.
#
# In a valid triangle, the sum of any two sides must be larger than the remaining side. 
# For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.
#
# In your puzzle input, how many of the listed triangles are possible?


# --- Part Two ---
#
# Now that you've helpfully marked up their design documents, it occurs to you that triangles 
# are specified in groups of three vertically. Each set of three numbers in a column 
# specifies a triangle. Rows are unrelated.
#
# For example, given the following specification, numbers with the same hundreds digit would
# be part of the same triangle:
#
# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603
#
# In your puzzle input, and instead reading by columns, how many of the listed triangles 
# are possible?

class Day3

  def self.how_many_are_possible(triangles)
    return triangles.count do |triangle|
      is_possible?(triangle)
    end
  end

  def self.is_possible?(triangle)
    sides = triangle.map(&:to_i).sort
    return (sides.size == 3 && (sides[0] + sides[1] > sides[2]))
  end
  
  def self.input_split_by_rows(input)
    input.split("\n").map do |row|
      row.strip.split(/\s+/)
    end
  end

  def self.input_split_by_columns(input)
    triangles = []
    input.split("\n").each_slice(3) do |rows|
      (x,y,z) = rows.map{|row| row.strip.split(/\s+/).map(&:to_i)}
      triangles.push([x[0],y[0],z[0]])
      triangles.push([x[1],y[1],z[1]])
      triangles.push([x[2],y[2],z[2]])
    end
    triangles
  end

  def self.main
    input = File.read("inputs/day3.txt")
    puts "Part 1: #{how_many_are_possible(input_split_by_rows(input))}"
    puts "Part 2: #{how_many_are_possible(input_split_by_columns(input))}"
  end

end

Day3.main
