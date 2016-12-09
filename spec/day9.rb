require 'spec_helper'
require './app/day9'

describe Day9 do
  
  describe "#one_level_decompress" do
    it "wprks with no markers" do
      expect(Day9.one_level_decompress("ADVENT")).to eq("ADVENT")
    end

    it "ex2 " do
      expect(Day9.one_level_decompress("A(1x5)BC")).to eq("ABBBBBC")
    end

    it "ex 3" do
      expect(Day9.one_level_decompress("(3x3)XYZ")).to eq("XYZXYZXYZ")
    end

    it "ex 4" do
      expect(Day9.one_level_decompress("A(2x2)BCD(2x2)EFG")).to eq("ABCBCDEFEFG")
    end

    it "ex 5" do
      expect(Day9.one_level_decompress("(6x1)(1x3)A")).to eq("(1x3)A")
    end
    
    it "ex 6" do
      expect(Day9.one_level_decompress("X(8x2)(3x3)ABCY")).to eq("X(3x3)ABC(3x3)ABCY")
    end

    it "sample from file" do
      sample = "(4x14)JVWV(84x11)(24x2)YAFPPYWOQJKUKQTJACJAOWYF(25x11)(1x1)J(12x14)CNZKOSNAJVYL"
      expect(Day9.one_level_decompress(sample)).to eq("JVWVJVWVJVWVJVWVJVWVJVWVJVWVJVWVJVWVJVWVJVWVJVWVJVWVJVWV(24x2)YAFPPYWOQJKUKQTJACJAOWYF(25x11)(1x1)J(12x14)CNZKOSNAJVYL(24x2)YAFPPYWOQJKUKQTJACJAOWYF(25x11)(1x1)J(12x14)CNZKOSNAJVYL(24x2)YAFPPYWOQJKUKQTJACJAOWYF(25x11)(1x1)J(12x14)CNZKOSNAJVYL(24x2)YAFPPYWOQJKUKQTJACJAOWYF(25x11)(1x1)J(12x14)CNZKOSNAJVYL(24x2)YAFPPYWOQJKUKQTJACJAOWYF(25x11)(1x1)J(12x14)CNZKOSNAJVYL(24x2)YAFPPYWOQJKUKQTJACJAOWYF(25x11)(1x1)J(12x14)CNZKOSNAJVYL(24x2)YAFPPYWOQJKUKQTJACJAOWYF(25x11)(1x1)J(12x14)CNZKOSNAJVYL(24x2)YAFPPYWOQJKUKQTJACJAOWYF(25x11)(1x1)J(12x14)CNZKOSNAJVYL(24x2)YAFPPYWOQJKUKQTJACJAOWYF(25x11)(1x1)J(12x14)CNZKOSNAJVYL(24x2)YAFPPYWOQJKUKQTJACJAOWYF(25x11)(1x1)J(12x14)CNZKOSNAJVYL(24x2)YAFPPYWOQJKUKQTJACJAOWYF(25x11)(1x1)J(12x14)CNZKOSNAJVYL")
    end
    
  end

  describe "#decompressed_length" do
    
    # (3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no markers.
    it "ex 1" do
      expect(Day9.decompressed_length("(3x3)XYZ")).to eq(9)
    end

    # X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data 
    # from the (8x2) marker is then further decompressed, thus triggering the (3x3) marker
    # twice for a total of six ABC sequences.
    it "ex 2" do
      expect(Day9.decompressed_length("X(8x2)(3x3)ABCY")).to eq(20)
    end

    # (27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated 241920 times.
    it "ex 3" do
      expect(Day9.decompressed_length("(27x12)(20x12)(13x14)(7x10)(1x12)A")).to eq(241920)
    end

    # (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 characters long.
    it "ex 4" do
      expect(Day9.decompressed_length("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN")).to eq(445)
    end

    # should be ABC(2ABCABABAB
    it "handles new closures that span repeated segments and new" do
      expect(Day9.decompressed_length("(5x2)ABC(2x3)AB")).to eq(15)
    end
    
  end

end
