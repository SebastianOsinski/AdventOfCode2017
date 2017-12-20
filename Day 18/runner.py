from program import Program

class Runner:

    def __init__(self, program0, program1):
        self.program0 = program0
        self.program1 = program1

    def run(self):
        while self.program0.can_run() or self.program1.can_run():
            self.program0.run()
            self.program1.run()