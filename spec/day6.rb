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
    
    #
    # For example, suppose you had recorded the following messages:
    #
    # eedadn
    # drvtee
    # eandsr
    # raavrd
    # atevrs
    # tsrnev
    # sdttsa
    # rasrtv
    # nssdts
    # ntnada
    # svetve
    # tesnvt
    # vntsnd
    # vrdear
    # dvrsen
    # enarar
    # 
    # The most common character in the first column is e; in the second, a; 
    # in the third, s, and so on. Combining these characters returns the 
    # error-corrected message, easter.

    it "sample input works" do
      expect(Day6.error_corrected_message(sample_input)).to eq("easter")
    end
    
  end

  describe "part 2" do

    # In the above example, the least common character in the first column is a; 
    # in the second, d, and so on. Repeating this process for the remaining 
    # characters produces the original message, advent.
    
    it "sample input works" do
      expect(Day6.modified_repetition_error_corrected_message(sample_input)).to eq("advent")
    end
  end

end
