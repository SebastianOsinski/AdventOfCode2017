class Instruction:

  def __init__(self, register, operation, value, condition_register, condition, condition_value):
      self.register = register
      self.operation = operation
      self.value = value
      self.condition_register = condition_register
      self.condition = condition
      self.condition_value = condition_value