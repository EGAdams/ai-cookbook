# MarkdownFormatter Module

## Overview
The `MarkdownFormatter` module provides functionality to format strings and generate tables in Markdown syntax. It implements the `IMarkdownOutput` interface.

## Class Definitions

### IMarkdownOutput
This is an interface that defines methods for formatting text and generating tables in Markdown, to be implemented by any Markdown output class.

#### Methods:
- `format_text(text: str) -> str`: Formats the input text into Markdown style.
- `generate_table(headers: list, rows: list) -> str`: Generates a Markdown-formatted table from a list of headers and rows.

### MarkdownFormatter
This class implements the `IMarkdownOutput` interface and provides concrete implementations for formatting text and generating tables.

#### Methods:
- `format_text(text: str) -> str`: Converts input text into bold Markdown format by wrapping it with double asterisks **.
- `generate_table(headers: list, rows: list) -> str`: Creates a Markdown table from provided headers and rows.

## Usage
To utilize this module, instantiate the `MarkdownFormatter` class and call its methods for formatting text or generating tables.

```python
formatter = MarkdownFormatter()
formatted_text = formatter.format_text('Sample Text')

headers = ['Name', 'Age']
rows = [['Alice', 30], ['Bob', 25]]
markdown_table = formatter.generate_table(headers, rows)
```