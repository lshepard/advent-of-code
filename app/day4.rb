# --- Day 4: Security Through Obscurity ---
#
# Finally, you come across an information kiosk with a list of rooms. Of course, the list is
# encrypted and full of decoy data, but the instructions to decode the list are barely hidden
# nearby. Better remove the decoy data first.
#
# Each room consists of an encrypted name (lowercase letters separated by dashes) followed 
# by a dash, a sector ID, and a checksum in square brackets.
#
# A room is real (not a decoy) if the checksum is the five most common letters in the
# encrypted name, in order, with ties broken by alphabetization. For example:
#
#  aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), 
#     b (3), and then a tie between x, y, and z, which are listed alphabetically.
#  a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied 
#    (1 of each), the first five are listed alphabetically.
#  not-a-real-room-404[oarel] is a real room.
#  totally-real-room-200[decoy] is not.
#
# Of the real rooms from the list above, the sum of their sector IDs is 1514.
#
# What is the sum of the sector IDs of the real rooms?

class Day4

  def self.sum_of_sector_ids_of_real_rooms(input)
    input.split("\n").map do |line|
      data = split_room_line(line)
      if checksum_correct?(data)
        data[:sector_id].to_i
      else
        0
      end
    end.reduce(&:+)
  end


  # A room is real (not a decoy) if the checksum is the five most common letters in the
  # encrypted name, in order, with ties broken by alphabetization.
  def self.checksum_correct?(data)
    # five most common letters
    five_most_common_letters(data[:encrypted_name]) == data[:checksum]
  end
  
  def self.five_most_common_letters(name)
    name
      .gsub(/-/,'')
      .chars
      .inject(Hash.new(0)) { |h, x| h[x] += 1; h}
      .sort_by {|letter, count| [-count, letter]}
      .take(5)
      .map(&:first)
      .join('')
  end

  def self.split_room_line(line)
    matches = /([-a-z]+)-(\d+)\[([a-z]+)\]/.match(line)
    
    {
      encrypted_name: matches[1],
      sector_id: matches[2],
      checksum: matches[3]
    }
  end
  
  def self.main
    input = File.read("inputs/day4.txt")
    puts "Part 1: #{sum_of_sector_ids_of_real_rooms(input)}"
  end
end
