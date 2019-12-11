from itertools import cycle

# An Intcode program is a list of integers separated by commas (like 1,0,0,3,99). To run one,
# start by looking at the first integer (called position 0). Here, you will find an
# opcode - either 1, 2, or 99. The opcode indicates what to do; for example, 99 means
# that the program is finished and should immediately halt. Encountering an unknown opcode means something went wrong.

# Opcode 1 adds together numbers read from two positions and stores the result in a third position. The three integers immediately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the position at which the output should be stored.

# For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20, add those values, and then overwrite the value at position 30 with their sum.


# Once you're done processing an opcode, move to the next one by stepping forward 4 positions.

class IntCodeComputer():

    def __init__(self, memory):
        self.memory = [int(i) for i in memory.split(",")]
        self.i = 0
        self.done = False
        self.input = None
        self.outputs = []
        self.phase_setting = None
        self.relative_base = 0

    def __repr__(self):
        return f"i:{self.i} done:{self.done} input:{self.input} outputs:{self.outputs} mem:{self.memory}"

    def set_phase_setting(self, phase_setting):
        self.phase_setting = phase_setting
    
    def set_relative_base(self, b):
        self.relative_base = b
        
    def add_input(self, input):
        self.input = input
        
    def parameter_mode(self, operation, n):
        s = str(operation)
        if n > len(s) - 2:
            return 0
        else:
            return int(s[len(s)-2-n])


    def get_parameter(self, i, param_num, force_immediate=False):
        mode = self.parameter_mode(self.memory[i], param_num)
        raw_value = self.memory[i + param_num]
        #print(f"i:{i} param_num:{param_num} mode:{mode} raw:{raw_value} memory:{self.memory}")
        
        try:
            # TODO clean this up
            if force_immediate:
                if mode == 1 or mode == 0:
                    return raw_value
                elif mode == 2:
                    return raw_value + self.relative_base
                
            else:
            
                if mode == 1: # immediate mode
                    return raw_value
                elif mode == 0: # position mode
                    return self.memory[raw_value]
                elif mode == 2: # relative mode
                    return self.memory[raw_value + self.relative_base]
        except IndexError:
            return 0

        

    def write_mem(self, location, value):
#        print(f"location:{location} length:{len(self.memory)}")

        
        if location >= len(self.memory):
            print("writing more ...")
            for i in range(len(self.memory), location+10):
                self.memory.append(0)

            print(f"location:{location} length:{len(self.memory)}")

        self.memory[location] = int(value)
                
    def add_output(self, val):
        self.outputs.append(val)

    def compute(self):
        while True:
            next_i = self.process_instruction(self.i)

            # so we can return for two reasons:
            # first is waiting for input. in which case we return
            # the current output and put this on pause. We'll resume later

            # the other reasons is that the program is truly done
            if next_i == -1: # sentinel meaning more input needed
                print("next i is -1")
                return self.output()
            if next_i is None:
                self.done = True
                return self.output()
            
            self.i = next_i

    def isdone(self):
        return self.done

    def clear_output(self):
        self.outputs = []
        
    def outputs_and_clear(self):
        out = self.outputs
        self.outputs = []
        return out
    
    def output(self):
        return ",".join([str(i) for i in self.outputs])

    def first_location(self):
        return self.memory[0]

    # Basically, I want it to get the phase setting the first time,
    # and each subsequent time to get a new input.
    # i could have it just wait.
    def get_input(self):
        if self.phase_setting:
            # one time only
            v = self.phase_setting
            self.phase_setting = None
        else:
            v = self.input
        return v
        
    def process_instruction(self, i):
        """Process, and Returns the next instruction location"""
        instruction = str(self.memory[i])
        opcode = int(instruction[-2:])

        #print(f"i:{i} instruction:{instruction} opcode:{opcode} outputs:{self.outputs} memory:{self.memory}")

        # Opcode 1 adds together numbers read from two positions and stores
        # the result in a third position. The three integers immediately
        # after the opcode tell you these three positions - the first two
        # indicate the positions from which you should read the input values,
        # and the third indicates the position at which the output should be stored.
        if opcode == 1:
            output = self.get_parameter(i, 1) + self.get_parameter(i, 2)
            self.write_mem(self.get_parameter(i, 3, force_immediate=True), output)
            return i+4
            
        # Opcode 2 works exactly like opcode 1, except it multiplies the two inputs
        # instead of adding them. Again, the three integers after the opcode indicate
        # where the inputs and outputs are, not their values.
        elif opcode == 2:
            output = self.get_parameter(i, 1) * self.get_parameter(i, 2)
            self.write_mem(self.get_parameter(i, 3, force_immediate=True), output)
            return i+4

        elif opcode == 3:
            inp = self.get_input()
            p = self.get_parameter(i, 1, force_immediate=True)
#            mode = self.parameter_mode(self.memory[i], 1)
            # writing memory is a bit trick,y i need to reimplement here
#            if mode == 2:
#                p = p+self.relative_base
            self.write_mem(p, inp)
            return i+2
            
        elif opcode == 4:
            p = self.get_parameter(i, 1)
            self.add_output(p)
            self.i = i+2
            print(f"setting output {p}")
            return -1

        elif opcode == 5:
            if self.get_parameter(i, 1) != 0:
                return self.get_parameter(i, 2)
            else:
                return i+3

        elif opcode == 6:
            if self.get_parameter(i, 1) == 0:
                return self.get_parameter(i, 2)
            else:
                return i+3

        elif opcode == 7: # less than
            if self.get_parameter(i, 1) < self.get_parameter(i, 2):
                val = 1
            else:
                val = 0
                
            self.write_mem(self.get_parameter(i, 3, force_immediate=True), val)
            return i+4

        elif opcode == 8: # less than
            if self.get_parameter(i, 1) == self.get_parameter(i, 2):
                val = 1
            else:
                val = 0
                
            self.write_mem(self.get_parameter(i, 3, force_immediate=True), val)
            return i+4

        elif opcode == 9:
            self.set_relative_base(self.relative_base + self.get_parameter(i, 1))
            
            return i+2
            
        elif opcode == 99:
            return None

        else:
            assert("This is not a corect opcode" + str(opcode) + " at position " + str(i))
          
        
    
# provided unit tests
#assert(compute("1,0,0,0,99") == "2,0,0,0,99")
#assert(compute("2,3,0,3,99") == "2,3,0,6,99")
#assert(compute("2,4,4,5,99,0") == "2,4,4,5,99,9801")
#assert(compute("1,1,1,4,99,5,6,0,99") == "30,1,1,4,2,5,6,0,99")

#assert(parameter_mode("1001",1) == 0)
#assert(parameter_mode("1001",2) == 1)

# my provided input
input = "3,225,1,225,6,6,1100,1,238,225,104,0,1102,7,85,225,1102,67,12,225,102,36,65,224,1001,224,-3096,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1001,17,31,224,1001,224,-98,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,86,19,225,1101,5,27,225,1102,18,37,225,2,125,74,224,1001,224,-1406,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1102,13,47,225,1,99,14,224,1001,224,-98,224,4,224,102,8,223,223,1001,224,2,224,1,224,223,223,1101,38,88,225,1102,91,36,224,101,-3276,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1101,59,76,224,1001,224,-135,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,101,90,195,224,1001,224,-112,224,4,224,102,8,223,223,1001,224,7,224,1,224,223,223,1102,22,28,225,1002,69,47,224,1001,224,-235,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,226,226,224,102,2,223,223,1006,224,329,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,344,101,1,223,223,108,677,226,224,102,2,223,223,1006,224,359,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,374,101,1,223,223,1008,677,226,224,1002,223,2,223,1006,224,389,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,404,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,419,101,1,223,223,7,226,226,224,102,2,223,223,1005,224,434,1001,223,1,223,8,226,226,224,1002,223,2,223,1006,224,449,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,464,101,1,223,223,1007,226,677,224,1002,223,2,223,1006,224,479,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,677,677,224,102,2,223,223,1005,224,509,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,524,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,554,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,569,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,584,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,599,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,614,101,1,223,223,1107,226,677,224,102,2,223,223,1006,224,629,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,226,226,224,102,2,223,223,1005,224,659,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226"

#s = IntCodeComputer("3,0,4,0,99", "5").compute()
#assert(s.output() == "5")
#assert(IntCodeComputer("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99", "5").compute().output() == "999")
