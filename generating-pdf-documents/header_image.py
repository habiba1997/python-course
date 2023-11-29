# fpdf help in generating pdf
from fpdf import FPDF
import os

try:
    os.remove("sample.pdf")
finally:
    pass


# note to add header or image => I need to overide some methods of fpdf class => meaning I need to create a class

class PDF(FPDF):
    def header(self):
        self.image("download.jpg", 10, 8, 33)
        self.set_font("helvetica", "B", 16)
        self.cell(40)
        self.cell(40, 10, "hello world", border=1, align="C")


pdf = PDF()
pdf.add_page()
pdf.output("sample.pdf")
