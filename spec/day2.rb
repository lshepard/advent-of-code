require 'spec_helper'
require './app/day2'

describe Day2 do

  describe "part 1" do
    let(:input) {"ULL\nRRDDD\nLURDL\nUUUUD"}

    it "simple keypad apply move" do
      expect(Day2.bathroom_code(input, :simple_keypad_apply_move)).to eq("1985")
    end

    it "complex keypad apply move" do
      expect(Day2.bathroom_code(input, :complex_keypad_apply_move)).to eq("5DB3")
    end
  end

  describe "simple_keypad_apply_move" do
    it "applies to 5" do
      expect(Day2.simple_keypad_apply_move(5, "U")).to eq(2)
    end

    it "applies to 9" do
      expect(Day2.simple_keypad_apply_move(9, "R")).to eq(9)
    end
  end

  describe "complex_keypad_apply_move" do
    it "given ex 1" do
      expect(Day2.complex_keypad_apply_move(5, "U")).to eq(5)
    end

    it "applies to B" do
      expect(Day2.complex_keypad_apply_move("B", "R")).to eq("C")
    end
  end

  describe "digit_for_row" do
    it "5 ULL" do
      expect(Day2.digit_for_row(5, "ULL".chars, :simple_keypad_apply_move)).to eq(1)
    end

    it "9 RRRUUULLLDDDRRR" do
      expect(Day2.digit_for_row(9, "RRRUUULLLDDDRRR".chars, :simple_keypad_apply_move)).to eq(9)
    end
  end

  describe "remaining codes" do
    it "works with multiple rows" do
      expect(Day2.remaining_codes(1, ["R","R","D","LL"], :simple_keypad_apply_move)).to eq([2,3,6,4])
    end
  end
end
