"""
Interleave PDF pages

This script takes a scanned PDF where the first half contains the front pages
and the second half contains the back pages in reverse order.
It rearranges the pages into the correct interleaved order.
"""

import sys

import pymupdf  # PyMuPDF


def interleave_pdf(input_pdf, output_pdf):
    # Open the input PDF
    doc = pymupdf.open(input_pdf)
    total_pages = len(doc)

    if total_pages % 2 != 0:
        print(
            "Warning: The PDF has an odd number of pages. The last page might not have a back side."
        )

    mid = total_pages // 2
    front_pages = list(range(mid))  # First half (front pages)
    back_pages = list(
        range(total_pages - 1, mid - 1, -1)
    )  # Second half (back pages in reverse order)

    # Create a new output PDF
    output_doc = pymupdf.open()

    for front, back in zip(front_pages, back_pages):
        output_doc.insert_pdf(doc, from_page=front, to_page=front)
        output_doc.insert_pdf(doc, from_page=back, to_page=back)

    # If there's an extra page, add it at the end
    if total_pages % 2 != 0:
        output_doc.insert_pdf(doc, from_page=total_pages - 1, to_page=total_pages - 1)

    output_doc.save(output_pdf)
    print(f"Interleaved PDF saved as: {output_pdf}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python interleave_pdf.py input.pdf output.pdf")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_pdf = sys.argv[2]
    interleave_pdf(input_pdf, output_pdf)
