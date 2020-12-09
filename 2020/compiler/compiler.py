
class UnknownInstructionError(Exception):
    """Thrown if we reach an exception we didn't expect"""
    def __init__(self, line, line_num):
        self.line = line
        self.line_num = line_num
        self.message = f"Unknown instruction at {line_num}: {line}"
        super().__init__(self.message)

class ParseError(Exception):
    """Thrown if we reach an exception we didn't expect"""
    def __init__(self, line, line_num):
        self.line = line
        self.line_num = line_num
        self.message = f"Parse error at {line_num}: {line}"
        super().__init__(self.message)

class Compiler():
    def __init__(self, code=None):
        self.accumulator = 0
        self.code = None
        if code:
            self.set_code(code)

    def set_code(self, code):
        self.code = code.split("\n")

    def execute_to_no_repeat(self):
        """Executes until a line is repeated then returns the accumulator.
        Used for part 1 of day 8."""

        lines_seen = set()
        line_num = 0
        while True:
            if line_num in lines_seen:
                return self.accumulator
            
            lines_seen.add(line_num)
            line_num = self.execute_line(line_num)
        
    def execute(self):
        """Executes an entire program to completion."""
        line_num = 0
        while line_num < len(self.code):
            line_num = self.execute_line(line_num)
            
        if line_num > len(self.code): # if we have been asked to go past the end of the file
            raise IndexError("Program extended beyond the end of the file to line " + line_num)

    def execute_line(self, line_num):
        """Runs the line at number, and returns the next line number to run."""
        if line_num >= len(self.code):
            raise IndexError("Line beyond code " + line_num + " code length " + len(self.code))
        
        line = self.code[line_num].strip()
        try:
            inst, val = line.split(" ")
        except:
            raise ParseError(line, line_num)
        
        if inst == "acc":
            self.accumulator += int(val)
            return line_num + 1
        
        elif inst == "jmp":
            return line_num + int(val)
        
        elif inst == "nop":
            return line_num + 1
        else:
            raise UnknownInstructionError(line, line_num)

    @staticmethod
    def run(code):
        """Runs the given code to completion and returns the accumulator"""

        c = Compiler(code)
        c.execute()
        return c.accumulator

