class Day9

  # The format compresses a sequence of characters. Whitespace is ignored. 
  # To indicate that some sequence should be repeated, a marker is added 
  # to the file, like (10x2). To decompress this marker, take the subsequent 
  # 10 characters and repeat them 2 times. Then, continue reading the file 
  # after the repeated data. 
  #
  # The marker itself is not included in the decompressed output.
  #
  # If parentheses or other characters appear within the data referenced by 
  # a marker, that's okay - treat it like normal data, not a marker, and then
  # resume looking for markers after the decompressed section.
  def self.one_level_decompress(input)
    if (m = /\((\d+)x(\d+)\)/.match(input))
      orig_char_count = m[1]
      multiplier = m[2]
      found_position = m.begin(0)
      last_position = m.end(0)
      chars_to_repeat = input.slice(m.end(0).to_i, orig_char_count.to_i)
      decoded = chars_to_repeat * multiplier.to_i
      
      remaining = input.slice(m.end(0) + orig_char_count.to_i, input.length) || ""
      input.slice(0,m.begin(0)) + decoded + one_level_decompress(remaining)
    else
      input
    end
  end
  
  # In version two, the only difference is that markers within decompressed 
  # data are decompressed. This, the documentation explains, provides much 
  # more substantial compression capabilities, allowing many-gigabyte files 
  # to be stored in only a few kilobytes.
  #
  # Unfortunately, the computer you brought probably doesn't have enough memory
  # to actually decompress the file; you'll have to come up with another way to
  # get its decompressed length.
  def self.decompressed_length(input)
    if (m = /\((\d+)x(\d+)\)/.match(input))
      count = m[1].to_i
      multiplier = m[2].to_i
      
      m.begin(0) + 
        multiplier * decompressed_length(input.slice(m.end(0), count)) +
        decompressed_length(input.slice(m.end(0) + count, input.length))
    else
      input.length
    end
  end

  def self.main
    input = File.read("inputs/day9.txt")
    puts "Part 1: #{Day9.one_level_decompress(input.chomp).length}"
    puts "Part 2: #{Day9.decompressed_length(input.chomp)}"
  end

end

if __FILE__==$0
  Day9.main
end
