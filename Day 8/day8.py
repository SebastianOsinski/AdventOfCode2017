import re
from cpu import CPU
from instruction import Instruction

file = open("day8_input", "r")

pattern = re.compile("([a-z]+) (inc|dec) (-?\d+) if ([a-z]+) (<|<=|==|!=|>=|>) (-?\d+)")

cpu = CPU()

for line in file:
    match = pattern.match(line)
    register = match.group(1)
    operation = match.group(2)
    value = int(match.group(3))
    condition_register = match.group(4)
    condition = match.group(5)
    condition_value = int(match.group(6))

    instruction = Instruction(register, operation, value, condition_register, condition, condition_value)
    cpu.execute_instruction(instruction)

print(cpu.find_largest_register_value())
print(cpu.lifetime_max)