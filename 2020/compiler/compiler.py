import logging
logging.basicConfig(format='[L] %(message)s',level=logging.DEBUG)

class Compiler():
    """Encapsulates the compiler that is defined in AOC day 8"""
    def __init__(self, code=None):
        self.accumulator = 0
        self.code = None
        if code:
            self.set_code(code)

    def set_code(self, code):
        if isinstance(code, list):
            self.code = code
        elif isinstance(code, str):
            self.code = code.split("\n")
        else:
            raise ValueError("Invalid value for code")

    def execute(self, raise_on_repeat=False):
        """Executes until the end of the file. Possible raises an error if lines are repeated."""

        lines_seen = set()
        line_num = 0
        while line_num < len(self.code):
            if line_num in lines_seen:
                raise RepeatedLineError()
            
            lines_seen.add(line_num)
            line_num = self.execute_line(line_num)
            
        return self.accumulator

    def execute_line(self, line_num):
        """Runs the line at number, and returns the next line number to run."""
        if line_num >= len(self.code):
            raise IndexError("Line beyond code " + line_num + " code length " + len(self.code))

        line = self.code[line_num].strip()
        logging.info(str(line_num) + ":\tacc=" + str(self.accumulator) + "  \t" + line)
        
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

class RepeatedLineError(Exception):
    pass
