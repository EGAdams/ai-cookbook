# markdown_formatter.py

class IMarkdownOutput:
    """
    Interface for Markdown Output
    """ 

    def format_text(self, text: str) -> str:
        """
        Method to format text in Markdown style.
        """ 
        pass

    def generate_table(self, headers: list, rows: list) -> str:
        """
        Method to generate a Markdown table from headers and rows.
        """ 
        pass

class MarkdownFormatter(IMarkdownOutput):
    
    def format_text(self, text: str) -> str:
        """
        Format the input text to Markdown style.
        """ 
        # Example: converting text to bold
        return f'**{text}**'
    
    def generate_table(self, headers: list, rows: list) -> str:
        """
        Generate a Markdown table from headers and rows.
        """ 
        if not headers or not rows:
            return "" 
 
        # Create table header
        header_line = " | ".join(headers) + " \n"
        separator_line = " | ".join(['---' for _ in headers]) + " \n" 
        # Create rows
        row_lines = []
        for row in rows:
            row_lines.append(" | ".join(map(str, row)) + " \n")

        # Combine all parts
        return header_line + separator_line + "".join(row_lines)