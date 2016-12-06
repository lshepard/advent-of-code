# --- Day 6: Signals and Noise ---
#
# Something is jamming your communications with Santa. Fortunately, your signal is
# only partially jammed, and protocol in situations like this is to switch to a
# simple repetition code to get the message through.

# In this model, the same message is sent repeatedly. You've recorded the repeating
# message signal (your puzzle input), but the data seems quite corrupted - almost too 
# badly to recover. Almost.
#
class Day6

  # All you need to do is figure out which character is most frequent for each position.
  # The most common character in the first column is e; in the second, a; 
  # in the third, s, and so on. Combining these characters returns the 
  # error-corrected message, easter.
  def self.error_corrected_message(input)
    transpose_and_count(input, :max_by)
  end
  
  #
  # --- Part Two ---
  # 
  # Of course, that would be the message - if you hadn't agreed to use a modified
  # repetition code instead.
  #
  # In this modified code, the sender instead transmits what looks like random 
  # data, but for each character, the character they actually want to send is 
  # slightly less likely than the others. Even after signal-jamming noise, you can
  # look at the letter distributions in each column and choose the least common 
  # letter to reconstruct the original message.
  # 
  def self.modified_repetition_error_corrected_message(input)
    transpose_and_count(input, :min_by)
  end

  # Takes a newline-delimited series of strings, then transposes them by columns,
  # evaluates each column according to the column_eval_fn, then joins the results
  def self.transpose_and_count(input, column_eval_fn)
    input.split("\n").map {|row| row.strip.split(//)}.transpose.map do |column|
      counts = column.inject(Hash.new(0)) { |h, x| h[x] += 1; h}
      column.send(column_eval_fn, &lambda {|v| counts[v]})
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
