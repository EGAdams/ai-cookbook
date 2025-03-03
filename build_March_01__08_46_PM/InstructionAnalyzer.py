import re
from markdown2 import markdown

class ITextParser:
    def parse(self, text: str):
        raise NotImplementedError("Subclasses must implement this method")

class InstructionAnalyzer(ITextParser):
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.instructions = {'installation': '', 'build': ''}

    def read_file(self):
        with open(self.filepath, 'r') as file:
            return file.read()

    def extract_instructions(self, content: str):
        # Convert Markdown to plain text for easier regex processing.
        plain_text = markdown(content)
        self.instructions['installation'] = self.extract_section(plain_text, 'Installation')
        self.instructions['build'] = self.extract_section(plain_text, 'Build')

    def extract_section(self, text: str, section_title: str):
        # Regex to capture the section content
        pattern = re.compile(r'(?i){}\s*([^#]*)'.format(re.escape(section_title)))
        match = pattern.search(text)
        if match:
            return match.group(1).strip()
        return ''

    def parse(self):
        content = self.read_file()
        self.extract_instructions(content)
        return self.instructions
