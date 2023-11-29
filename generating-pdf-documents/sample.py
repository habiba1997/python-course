# fpdf help in generating pdf
from fpdf import FPDF
import os

try:
    os.remove("sample.pdf")
finally:
    pass

# check constructor for default values
pdf = FPDF()

pdf.add_page()
pdf.cell(40, 10, "hello word")
pdf.set_font("helvetica", "B", 16)
pdf.output("sample.pdf")

# note to add header or image => I need to overide some methods of fpdf class => meaning I need to create a class
