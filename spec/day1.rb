require 'spec_helper'
require './app/day1'

describe Day1 do

  it "ex 1" do
    expect(Day1.shortest_path(["R2","L3"])).to eq(5)
  end

  it "ex 2" do
    expect(Day1.shortest_path(["R2","R2","R2"])).to eq(2)
  end

  it "ex 3" do
    expect(Day1.shortest_path(["R5","L5","R5","R3"])).to eq(12)
  end

end
