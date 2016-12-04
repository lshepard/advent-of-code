require 'spec_helper'
require './app/day4'

describe Day4 do

  describe "part 1" do

    
    
  end

  describe "split_room_line" do
    
    it "first ex" do
      expect(Day4.split_room_line("aaaaa-bbb-z-y-x-123[abxyz]")
             ).to eq({encrypted_name: "aaaaa-bbb-z-y-x",
                       sector_id: "123",
                       checksum: "abxyz"})
    end
  end

  describe "five_most_common_letters" do
    it "simple" do
      expect(Day4.five_most_common_letters("aa-bb-cc-dd-ee")).to eq("abcde")
    end

    it "takes only 5" do
      expect(Day4.five_most_common_letters("f-g-aa-bb-cc-dd-ee")).to eq("abcde")
    end

    it "breaks tie by alphabetization" do
      expect(Day4.five_most_common_letters("ff-g-aaa-bbb-cc-dd-ee")).to eq("abcde")
    end
  end

  describe "checksum correct" do
    it "ex 1" do
      expect(Day4.checksum_correct?({encrypted_name: "aaaaa-bbb-z-y-x",
                                      sector_id: 123,
                                      checksum: "abxyz"})).to be_truthy
    end
    
    it "ex 2" do
      expect(Day4.checksum_correct?({encrypted_name: "a-b-c-d-e-f-g-h",
                                      sector_id: 987,
                                      checksum: "abcde"})).to be_truthy      
    end

    it "ex 3" do
      expect(Day4.checksum_correct?({encrypted_name: "not-a-real-room",
                                      sector_id: 404,
                                      checksum: "oarel"})).to be_truthy
    end

    it "ex 4" do
      expect(Day4.checksum_correct?({encrypted_name: "totally-real-room",
                                      sector_id: 200,
                                      checksum: "decoy"})).to be_falsey
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
end
