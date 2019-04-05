require 'spec_helper'
require './app/day5'

describe Day5 do

  describe "part 1" do
    
    it "hash" do
      expect(Day5.part1_password("abc")).to eq("18f47a30")
    end
    
  end

  describe "part 2" do
    
    it "hash" do
      expect(Day5.part2_password("abc")).to eq("05ace8e3")
    end
    
  end

end
