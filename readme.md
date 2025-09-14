# Interleave PDF files

This script reorders the pages of a PDF so they alternate between the first and second half of the document. It’s designed for situations where you’ve scanned a double-sided document in two passes—first all the front pages, then all the back pages in reverse order—and you need to merge them back into their correct sequence.

## Usage

```sh
poetry run python interleave_pdf.py input.pdf output.pdf
```
