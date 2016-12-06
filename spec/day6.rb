require 'spec_helper'
require './app/day6'

describe Day6 do

  let(:sample_input) {"eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"}

  describe "part 1" do
    
    it "sample input works" do
      expect(Day6.error_corrected_message(sample_input)).to eq("easter")
    end
    
  end

  describe "part 2" do
    it "sample input works" do
      expect(Day6.modified_repetition_error_corrected_message(sample_input)).to eq("advent")
    end
  end

end
