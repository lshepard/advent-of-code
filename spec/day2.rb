require 'spec_helper'
require './app/day2'

describe Day2 do

  describe "part 1" do
    let(:input) {"ULL\nRRDDD\nLURDL\nUUUUD"}

    it "ex 1" do
      expect(Day2.bathroom_code(input)).to eq(1985)
    end
  end
end
