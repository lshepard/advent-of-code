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
        c.set_input(input)
        c.compute()
        assert c.outputs == [expected_output]
    
    def test_day5_modes(self):
        # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        self.assert_program_with_input("3,9,8,9,10,9,4,9,99,-1,8", 8, 1) # == 8
        self.assert_program_with_input("3,9,8,9,10,9,4,9,99,-1,8", 7, 0) # != 8

        # Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
        self.assert_program_with_input("3,9,7,9,10,9,4,9,99,-1,8", 7, 1) # < 8
        self.assert_program_with_input("3,9,7,9,10,9,4,9,99,-1,8", 9, 0) # >= 8

        # Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        self.assert_program_with_input("3,3,1108,-1,8,3,4,3,99", 8, 1) # == 8
        self.assert_program_with_input("3,3,1108,-1,8,3,4,3,99", 7, 0) # != 8

        # Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
        self.assert_program_with_input("3,3,1107,-1,8,3,4,3,99", 7, 1) # < 8
        self.assert_program_with_input("3,3,1107,-1,8,3,4,3,99", 9, 0) # >= 8

    def assert_program_sequences(self, program, phase_sequences, loop_back, expected_output):

        computers = [IntCodeComputer(program) for i in range(len(phase_sequences))]
        for i, c in enumerate(computers):
            c.set_phase_setting(phase_sequences[i])
        
        keep_going = True
        value = 0
        while keep_going:
            
            for i, ps in enumerate(phase_sequences):
                c = computers[i]
                c.set_input(value)
                c.compute()
                value = c.output()

            if loop_back:
                keep_going = False
            elif (computers[0].isdone() and
                  computers[1].isdone() and
                  computers[2].isdone() and
                  computers[3].isdone() and
                  computers[4].isdone()):
                #all([c.isdone() for c in computers]):
                keep_going = False

        assert value == expected_output
            
    def test_day7_pt1(self):
        self.assert_program_sequences("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0",
                                      [4,3,2,1,0],
                                      False,
                                      "43210")
        
        self.assert_program_sequences("3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0",
                                      [0,1,2,3,4],
                                      False,
                                      "54321")

        
        self.assert_program_sequences("3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0",
                                      [1,0,4,3,2],
                                      False,
                                      "65210")

    def test_day7_pt2(self):
        self.assert_program_sequences("3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5",
                                      [9,8,7,6,5],
                                      True,
                                      "139629729")
