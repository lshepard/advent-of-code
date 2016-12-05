require 'digest'
#--- Day 5: How About a Nice Game of Chess? ---
#
# You are faced with a security door designed by Easter Bunny engineers 
# that seem to have acquired most of their security knowledge by watching hacking movies.

class Day5

  # The eight-character password for the door is generated one character 
  # at a time by finding the MD5 hash of some Door ID (your puzzle input)
  # and an increasing integer index (starting with 0).
  #
  # A hash indicates the next character in the password if its hexadecimal 
  # representation starts with five zeroes. If it does, the sixth character 
  # in the hash is the next character of the password.
  def self.part1_password(input)
    password = ''
    i = 0
    while password.length < 8
      hash = Digest::MD5.hexdigest(input.to_s + i.to_s)
      if hash[0..4] == "00000"
        password += hash[5]
        puts password
      end
      i += 1
    end
    password
  end

  def self.part2_password(input)
    password = "        "
    index = 0
    while password.include?(" ")
      hash = ::Digest::MD5.hexdigest(input.to_s + index.to_s)

      location = hash[5]
      new_character = hash[6]
      if hash[0..4] == "00000" &&
          /[0-7]/.match(location) &&  # discard invalid locations
          password[location.to_i] == " "   # only take the first valid one
          password.insert(location.to_i, new_character)
          password.slice!(location.to_i + 1)
      end
      index += 1
    end
    password
  end

  def self.main
    puts "Part 1: #{Day5.part1_password('wtnhxymk')}"
    puts "Part 2: #{Day5.part2_password('wtnhxymk')}"
  end

end

if __FILE__==$0
  Day5.main
end
