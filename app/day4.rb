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

#
# --- Part Two ---
#
# With all the decoy data out of the way, it's time to decrypt this list and get moving.
#
# The room names are encrypted by a state-of-the-art shift cipher, which is nearly
# unbreakable without the right software. However, the information kiosk designers at 
# Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.
#
# To decrypt a room name, rotate each letter forward through the alphabet a number of
# times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on.
#  Dashes become spaces.
#
# For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.
#
# What is the sector ID of the room where North Pole objects are stored?

class Day4

  def self.sum_of_sector_ids_of_real_rooms(input)
    input.split("\n").map do |line|
      data = split_room_line(line)
    end.select do |data|
      calculate_checksum(data[:encrypted_name]) == data[:checksum]
    end.map do |data|
      data[:sector_id].to_i
    end.reduce(&:+)
  end

  def self.sector_id_the_special_room(input, match_phrase)
    input.split("\n").map do |line| 
      split_room_line(line)
    end.select do |data|
      name =  decrypt_name(data[:encrypted_name], data[:sector_id].to_i)
      name == match_phrase
    end.first[:sector_id]
  end

  # A room is real (not a decoy) if the checksum is the five most common letters in the
  # encrypted name, in order, with ties broken by alphabetization.
  def self.calculate_checksum(name)
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
  
  # To decrypt a room name, rotate each letter forward through the alphabet a number of
  # times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on.
  #  Dashes become spaces.
  def self.decrypt_name(name, rotate_count)
    name.chars.map do |char|
      if char == "-"
        " "
      else
        ((((char.ord - "a".ord) + rotate_count) % 26) + "a".ord).chr
      end
    end.join("")
  end

  def self.main
    input = File.read("inputs/day4.txt")
    puts "Part 1: #{sum_of_sector_ids_of_real_rooms(input)}"
    puts "Part 2: #{sector_id_the_special_room(input, 'northpole object storage')}"
  end
end

Day4.main
