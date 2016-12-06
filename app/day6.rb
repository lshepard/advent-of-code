class Day6

  def self.error_corrected_message(input)
    input.split("\n").map {|row| row.strip.split(//)}.transpose.map do |column|
      counts = column.inject(Hash.new(0)) { |h, x| h[x] += 1; h}
      column.max_by { |v| counts[v] }
    end.join("")
  end

  def self.modified_repetition_error_corrected_message(input)
    input.split("\n").map {|row| row.strip.split(//)}.transpose.map do |column|
      counts = column.inject(Hash.new(0)) { |h, x| h[x] += 1; h}
      column.min_by { |v| counts[v] }
    end.join("")
  end

  def self.main
    input = File.read("inputs/day6.txt")
    puts "Part 1: #{Day6.error_corrected_message(input)}"
    puts "Part 1: #{Day6.modified_repetition_error_corrected_message(input)}"
  end

end

if __FILE__==$0
  Day6.main
end
