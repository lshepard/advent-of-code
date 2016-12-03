require 'spec_helper'
require './app/day3'

describe Day3 do

  describe "part 1" do
    
    it "is not possible" do
      expect(Day3.is_possible?([1,2,5])).to be_falsey
    end

    it "is possible" do
      expect(Day3.is_possible?([1,2,2])).to be_truthy
    end

    it "how many are possible" do
      expect(Day3.how_many_are_possible([[2,4,5],[3,5,68]])).to eq(1)
      
    end
  end
  
  describe "part 2" do
    it "split by columns" do
      input = "101 301 501\n102 302 502\n103 303 503\n201 401 601\n202 402 602\n203 403 603"
      expect(Day3.input_split_by_columns(input)).to eq([[101,102,103],
                                                        [301,302,303],
                                                        [501,502,503],
                                                        [201,202,203],
                                                        [401,402,403],
                                                        [601,602,603]])
    end
  end

end
