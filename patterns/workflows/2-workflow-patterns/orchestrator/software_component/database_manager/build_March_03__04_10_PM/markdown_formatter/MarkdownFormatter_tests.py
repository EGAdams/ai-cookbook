import unittest

class TestMarkdownFormatter(unittest.TestCase):
    
    def setUp(self):
        self.formatter = MarkdownFormatter()
    
    def test_format_text(self):
        self.assertEqual(self.formatter.format_text("Hello"), '**Hello**')
        self.assertEqual(self.formatter.format_text("Test"), '**Test**')
    
    def test_generate_table(self):
        headers = ['Header1', 'Header2', 'Header3']
        rows = [
            ["Row1Col1", "Row1Col2", "Row1Col3"],
            ["Row2Col1", "Row2Col2", "Row2Col3"]
        ]
        expected_output = "Header1 | Header2 | Header3 \n" 
        expected_output += "--- | --- | --- \n" 
        expected_output += "Row1Col1 | Row1Col2 | Row1Col3 \n"
        expected_output += "Row2Col1 | Row2Col2 | Row2Col3 \n"
        
        self.assertEqual(self.formatter.generate_table(headers, rows), expected_output)
        
    def test_generate_empty_table(self):
        self.assertEqual(self.formatter.generate_table([], []), '')

if __name__ == '__main__':
    unittest.main()