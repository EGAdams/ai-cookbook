import unittest
from unittest.mock import mock_open, patch

class TestInstructionAnalyzer(unittest.TestCase):
    def test_extract_instructions(self):
        mock_readme_content = '''# Project Title\n\n## Installation\nRun `pip install package`\n\n## Build\nUse `make build` to compile the project.\n'''
        analyzer = InstructionAnalyzer('README.md')
        with patch('builtins.open', mock_open(read_data=mock_readme_content)):
            instructions = analyzer.parse()  
            self.assertEqual(instructions['installation'], 'Run `pip install package`')
            self.assertEqual(instructions['build'], 'Use `make build` to compile the project.')

if __name__ == '__main__':
    unittest.main()