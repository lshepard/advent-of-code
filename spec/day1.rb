require 'spec_helper'
require './app/day1'

describe Day1 do

  describe "part 1 - shortest path to end" do
    it "ex 1" do
      expect(Day1.shortest_path_from_origin(["R2","L3"])).to eq(5)
    end
    
    it "ex 2" do
      expect(Day1.shortest_path_from_origin(["R2","R2","R2"])).to eq(2)
    end
    
    it "ex 3" do
      expect(Day1.shortest_path_from_origin(["R5","L5","R5","R3"])).to eq(12)
    end
    
    it "multiple chars" do
      expect(Day1.shortest_path_from_origin(["R5","L5","R50","R3"])).to eq(57)
    end
  end

  describe "part 2 - first place to visit twice" do

    it "ex 1" do
      expect(Day1.shortest_path_to_first_place_to_visit_twice(["R8", "R4", "R4", "R8"])).to eq(4)
    end
  end

end
