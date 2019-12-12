from intcode import IntCodeComputer

class TestIntCodeComputer():

    def c(self, program):
        return IntCodeComputer(program)

    def ints(self, stringtosplit):
        """Splits a string-delimited list into integers"""
        return [int(x) for x in stringtosplit.split(",")]

    def assert_program_memory_equals(self, program, memory):
        assert self.c(program).compute().memory == self.ints(memory)
        
    def test_day2(self):
        self.assert_program_memory_equals("1,0,0,0,99", "2,0,0,0,99")
        self.assert_program_memory_equals("2,3,0,3,99", "2,3,0,6,99")
        self.assert_program_memory_equals("2,4,4,5,99,0", "2,4,4,5,99,9801")
        self.assert_program_memory_equals("1,1,1,4,99,5,6,0,99", "30,1,1,4,2,5,6,0,99")


    def assert_program_with_input(self, program, input, expected_output):
        c = self.c(program)
        c.add_input(input)
        c.compute()
        assert c.outputs == [expected_output]
    
    def test_day5_1(self):
        # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        self.assert_program_with_input("3,9,8,9,10,9,4,9,99,-1,8", 8, 1) # == 8
        self.assert_program_with_input("3,9,8,9,10,9,4,9,99,-1,8", 7, 0) # != 8

    def test_day5_2(self):
        # Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
        self.assert_program_with_input("3,9,7,9,10,9,4,9,99,-1,8", 7, 1) # < 8
        self.assert_program_with_input("3,9,7,9,10,9,4,9,99,-1,8", 9, 0) # >= 8

    def test_day5_3(self):
        # Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        self.assert_program_with_input("3,3,1108,-1,8,3,4,3,99", 8, 1) # == 8
        self.assert_program_with_input("3,3,1108,-1,8,3,4,3,99", 7, 1) # != 8

    def test_day5_4(self):
        # Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
        self.assert_program_with_input("3,3,1107,-1,8,3,4,3,99", 7, 1) # < 8
        self.assert_program_with_input("3,3,1107,-1,8,3,4,3,99", 9, 1) # >= 8
        
