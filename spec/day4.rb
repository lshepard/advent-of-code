require 'spec_helper'
require './app/day4'

describe Day4 do

  describe "split_room_line" do
    it "first ex" do
      expect(Day4.split_room_line("aaaaa-bbb-z-y-x-123[abxyz]")
             ).to eq({encrypted_name: "aaaaa-bbb-z-y-x",
                       sector_id: "123",
                       checksum: "abxyz"})
    end
  end

  describe "calculate_checksum" do
    it "simple" do
      expect(Day4.calculate_checksum("aa-bb-cc-dd-ee")).to eq("abcde")
    end

    it "takes only 5" do
      expect(Day4.calculate_checksum("f-g-aa-bb-cc-dd-ee")).to eq("abcde")
    end

    it "breaks tie by alphabetization" do
      expect(Day4.calculate_checksum("ff-g-aaa-bbb-cc-dd-ee")).to eq("abcde")
    end

    it "ex 1" do
      expect(Day4.calculate_checksum("aaaaa-bbb-z-y-x")).to eq("abxyz")
    end
    
    it "ex 2" do
      expect(Day4.calculate_checksum("a-b-c-d-e-f-g-h")).to eq("abcde")
    end

    it "ex 3" do
      expect(Day4.calculate_checksum("not-a-real-room")).to eq("oarel")
    end

    it "ex 4" do
      expect(Day4.calculate_checksum("totally-real-room")).not_to eq("decoy")
    end
  end

  describe "sum_of_sector_ids_of_real_rooms" do
    let(:input) {["aaaaa-bbb-z-y-x-123[abxyz]",
                  "a-b-c-d-e-f-g-h-987[abcde]",
                  "not-a-real-room-404[oarel]",
                  "totally-real-room-200[decoy]"].join("\n")}
    
    it "matches given example" do
      expect(Day4.sum_of_sector_ids_of_real_rooms(input)).to eq(1514)
    end
  end
  
  describe "decrypt name" do
    it "ex 1" do
      expect(Day4.decrypt_name("qzmt-zixmtkozy-ivhz", 343)).to eq("very encrypted name")
    end
  end
end
