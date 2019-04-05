require 'spec_helper'
require './app/day8'

describe Day8 do

  describe Cell do
    let(:cell) {Cell.new(0,5,10,20)}
    describe "#rotate" do
      
      it "rotates right" do
        expect(cell.rotate(5,0).coords).to eq([5,5])
      end

      it "rotates right and wraps" do
        expect(cell.rotate(51,0).coords).to eq([1,5])
      end

      it "rotates down" do
        expect(cell.rotate(0,10).coords).to eq([0,15])
      end

      it "rotates down and wraps" do
        expect(cell.rotate(0,51).coords).to eq([0,16])
      end
    end
  end

  describe Board do
    let(:board){Board.new(5,5)}

    it "is empty" do
      expect(board.cells.count).to eq(0)
    end

    describe "#rect" do
      it "adds 3x2" do
        board.rect(3,2)
        expect(board.to_s).to eq("###  \n###  \n     \n     \n     ")
      end

      it "takes #rect instruction" do
        board.execute_instruction("rect 4x2")
        expect(board.to_s).to eq("#### \n#### \n     \n     \n     ")
      end
    end

    describe "with a box there" do
      before :each do
        board.rect(3,2)
      end

      it "takes rotate x" do
        board.execute_instruction("rotate column x=1 by 1")
        expect(board.to_s).to eq("# #  \n###  \n #   \n     \n     ")
      end

      it "takes rotate y" do
        board.execute_instruction("rotate row y=0 by 4")
        expect(board.to_s).to eq("##  #\n###  \n     \n     \n     ")
      end
    end

  end
  
  
end
