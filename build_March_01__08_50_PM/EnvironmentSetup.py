import os
import subprocess
import sys

class ISetupInstructions:
    def read_instructions(self, filepath):
        """Read instructions from a specified file."""
        raise NotImplementedError

    def execute_instructions(self, instructions):
        """Execute the given instructions."""
        raise NotImplementedError

class EnvironmentSetup(ISetupInstructions):
    def read_instructions(self, filepath):
        with open(filepath, 'r') as file:
            return file.readlines()

    def execute_instructions(self, instructions):
        for instruction in instructions:
            self.run_instruction(instruction.strip())

    def run_instruction(self, instruction):
        if instruction.startswith('pip install'):
            self.install_package(instruction)
        elif instruction.startswith('virtualenv '):
            self.create_virtualenv(instruction)
        else:
            print(f'Ignoring unrecognized instruction: {instruction}')

    def install_package(self, instruction):
        package = instruction.split(' ')[2]  # Extract package name
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

    def create_virtualenv(self, instruction):
        env_name = instruction.split(' ')[2]  # Extract environment name
        subprocess.check_call(['virtualenv', env_name])

    def setup_environment(self, readme_path):
        instructions = self.read_instructions(readme_path)
        self.execute_instructions(instructions)